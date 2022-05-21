import multiprocessing as mp
import queue
import codecs
import sys


def lector(w,q):
    
    print('mensaje a encriptar')
    sys.stdin = open(0)
    input = sys.stdin.readline()
    print('leyendo del stdin: %s ' % q.get())
    w.send(input)
    w.close()
    

def lector_cola(r,q):

    input = r.recv()
    print('el 2 hijo leyo del pipe: %s ' % str(input))
    r.close()
    mensaje = rot13(str(input))
    q.put(mensaje)

    def rot13():
        codecs.encode('foobar', 'rot_13')

if __name__ == '__main__':
                                             
    r, w = mp.Pipe()
    q = mp.Queue()
    hijouno = mp.Process(target=lector, args= (w,q))
    hijodos = mp.Process(target=lector_cola, args= (r,q))
    hijouno.start()
    hijodos.start()
    hijouno.join()
    hijodos.join()