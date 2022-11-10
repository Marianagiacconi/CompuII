import argparse
import socket
import sys
import socket
import time


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-i', '--ipserver', help='Indica el servidor', type=str, action='store', required=True)
    parse.add_argument('-p', '--port', help='Indica el puerto', type=int, action='store', required=True)
    parse.add_argument('-n', '--numero', help='numero a calcular', type=int, action='store', required=True)

    args = parse.parse_args()
    server  = args.ipserver
    puerto = args.port
    sock_cliente = socket.socket()
    try:
        sock_cliente.connect((server, puerto))
    except:
        print('Puerto o Server erroneos')
        sys.exit()
    oper = [ args.numero]
    sock_cliente.send(str(oper).encode())
    respuesta = sock_cliente.recv(1024)
    print('Su resultado es: ',respuesta.decode())
    print('Operacion realizada, desconectando...')
    time.sleep(1)
    sock_cliente.close()
                

if __name__ == '__main__':
    main()