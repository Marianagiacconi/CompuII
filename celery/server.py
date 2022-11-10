import argparse
import socket
from threading import Thread

from task import log


#redis.Redis(host='localhost', port=6379, db=0)
def funcion_calculo(con,adr):
    tarea = eval(con.recv(1024).decode())
    if tarea[0].lower() == 'log':
        resultadoSum = log.delay(tarea[1], tarea[2])
        con.send(str(resultadoSum.get()).encode())
    
    else:
        con.send('Error')
    print(f'La operacion se ha consumado, el cliente {adr} se ha desconectado')
    
    
if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-i', '--ipserver', help='Ip en donde se va a atender al cliente', required=True, action='store')
    parse.add_argument('-p', '--port', help='Puerto en donde se va a atender al cliente', required=True, action='store')
    args = parse.parse_args()
    PORT = args.port
    SERVER = args.ipserver
    print(f'Conexion levantada en -puerto {PORT}, ip {SERVER}-')
    sock_server = socket.socket()
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_server.bind(((SERVER), int(PORT)))
    sock_server.listen(5)
    while True:
        con, adr = sock_server.accept()
        print('Se ha establecido conexion con el cliente: ', adr)
        thr = Thread(target=funcion_calculo, args=(con,adr))
        thr.start()
