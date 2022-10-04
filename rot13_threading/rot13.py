import multiprocessing as mp
import sys, threading


def rot13(mensaje):
    print("El mensaje recibido en la funcion de encriptar es: %s" % str(mensaje))
    encriptado = []
    for letra in mensaje[:-1]:
        desp = ord(letra) + 13
        if ord(letra) >= 97 and ord(letra) <= 122:
            if desp > 122:
                desp = desp - 122 + 97 - 1
        else:
            if desp > 90:
                desp = desp - 90 + 65 - 1
        lencriptada = chr(desp)
        encriptado.append(lencriptada)
    return "".join(encriptado)

def hijo_lector_stdin(w, q):
    print("Hijo solicita mensaje para escribir en el pipe")
    sys.stdin = open(0)
    input = sys.stdin.readline()
    w.send(input)
    w.close()
    print("El mensaje encriptado es: %s" % q.get())   

def hijo_lector_pipe_cola(r, q):
    print("Hijo esperando leer del pipe")
    input = r.recv()
    print("Hijo leyó del pipe: %s" % str(input))
    r.close()
    mensaje = rot13(str(input))
    q.put(mensaje)    

if __name__ == '__main__':
    r, w = mp.Pipe()
    q = mp.Queue()
    thread1 = threading.Thread(target = hijo_lector_stdin, args=(w, q))
    thread2 = threading.Thread(target = hijo_lector_pipe_cola, args=(r, q))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()