from argparse import ArgumentParser
import signal, os, mmap


parser = ArgumentParser()
parser.add_argument('-f', help="Open specified file")
args = parser.parse_args()
input1 = ""
area = mmap.mmap(-1, 1024)


def h1():
    area.seek(0)
    leido = area.read(1024)
    input1 = input('ingresa caracteres')
    if input1.__eq__==('bye'):
        os.kill(os.getpid, signal.SIGUSR1)


def h2():
    h2= os.fork()
 
def exit():
    os.kill(os.getpid(), signal. SIGUSR1)
    os.kill(os.getpid(), signal. SIGUSR2)
    exit()

def lee_may(h2, input1):
    print(input1.read(12))
    signal.signal(signal.SIGUSR1, lee_may)
    input1.seek(0)
    input1.write(input.decode().upper().encode())
    os.kill(os.getppid(), signal.SIGUSR1)
    signal.pause()
    exit()


def main(args):
    var= vars(args)
    global input1
    pid= os.fork()
    pidd= os.getpid()

    if pid == 0:
        signal.signal(signal.SIGUSR2,exit)
        h1()
    
    else:
        pidd = os.fork()
        if pidd == 0:
            signal.signal(signal.SIGUSR2,exit)
            signal.signal(signal.SIGUSR1,h2)
            signal.pause()
            signal.signal(signal.SIGUSR1,lee_may)

if __name__ == "__main__":
    main(args)
    