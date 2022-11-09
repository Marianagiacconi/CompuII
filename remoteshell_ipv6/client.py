import socket
import sys
import argparse
import time, sys
    
def client(h,p):
    if h == 'localhost':
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Fallo la creacion del socket")
            sys.exit()
    if h == '::1':
        try:
            s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        except socket.error:
            print("Fallo la creacion del socket")
            sys.exit()
        
    
    host = h
    port = p

    print("Conectando...")
    time.sleep(2)
    s.connect((host,port))
    print("Conectado")
    time.sleep(1)
    print("Esperando datos del servidor")
    while True:    
       
        msg = input("Ingrese comando a ejecutar:")
        s.send(msg.encode())
        print("Esperando datos del servidor")
        msg = s.recv(1024)
        print(msg.decode())
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Help")
    parser.add_argument("-ht","--host",required=True,help="Dirección IP del servidor")
    parser.add_argument("-p","--port", type=int,required=True,help="Numero de puerto del servidor")
    args = parser.parse_args()
    print(args.host,args.port)
    client(args.host,args.port)
