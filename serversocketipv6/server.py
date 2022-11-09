import socket
import threading
import subprocess


def servicio(direccion):
    s = socket.socket(direccion[0], direccion[1], direccion[2])
    s.bind((direccion[4]))
    s.listen(1)
    while True:
        print("==================")
        s2, addr = s.accept()
        print(addr)
        enviado = s2.recv(1024)

        proceso = subprocess.Popen([enviado], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out,err = proceso.communicate()
    
        response = out + err
        

        respuesta = response.decode()

        s2.send(respuesta.encode())
        print("==========enviado========")
        print(enviado)
        print("==========respuesta========")
        print(respuesta)


        s2.close()


if __name__ == "__main__":

    direcciones = socket.getaddrinfo("localhost", 5000, socket.AF_UNSPEC, socket.SOCK_STREAM)
    print(len(direcciones))
    
    hilos = []
    for direccion in direcciones:
        print(direccion[4])
        hilos.append(threading.Thread(target=servicio, args=(direccion,)))

    for h in hilos:
        h.start()
    for h in hilos:
        h.join()
