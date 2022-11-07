import socket
import argparse

parser = argparse.ArgumentParser(description="cliente")
parser.add_argument("-j", "--host", type=str, required=True, help="Ingrese la direccion ip del host")
parser.add_argument("-p", "--puerto", type=int, required=True, help="Ingrese el numero de puerto del host")
args = parser.parse_args()
HOST, PORT = args.host, args.port

with socket.socket(socket.AF_INET6,socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT)) 
    while True:
        print("test1")
        data = socket.recv(1024)
        print("test2")
        print(data)