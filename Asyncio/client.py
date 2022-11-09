import socket 
import argparse

parser = argparse.ArgumentParser(description=None)
parser.add_argument("--host", type=str, help="string")
parser.add_argument("--port", type=int, help="int")
args = parser.parse_args()

try:
    if( not args.port):
        direcciones = socket.getaddrinfo("127.0.0.1", "8888", socket.AF_UNSPEC, 1)
    else:
        direcciones = socket.getaddrinfo(args.host, args.port, socket.AF_UNSPEC, 1)
except ValueError:
    direcciones = socket.getaddrinfo("127.0.0.1", "8888", socket.AF_UNSPEC, 1)

for direccion in direcciones:
    s = socket.socket(direccion[0], direccion[1])
    print("Connected to :", direccion[4])
    s.connect((direccion[4]))
    comandostr = str(input("Write command: "))
    comando = bytearray(comandostr, encoding='utf-8')
    s.send(comando)
    response = s.recv(1024).decode("utf-8")
    print(f"Response: {response}")
    s.close()