import argparse
import time
import multiprocessing as mp
import os
import math

matriz = []
global args

def main():

    parser = argparse.ArgumentParser(description="-p Cantidad de procesos, -f Directorio, -c Funcion a ingresar: raiz, pot, log")

    parser.add_argument("-p", "--process", type=int, required=True, help="string")
    parser.add_argument("-f", "--inputfile", type=str, required=True, help="string")
    parser.add_argument("-c", "--calc", type=str, required=True, help="string")
    global args
    args = parser.parse_args()

    print('Command: %d' % args.process)
    print('Output File: %s' % args.inputfile)
    print('Log File: %s' % args.calc)
    if not (args.calc == 'pot' or args.calc == 'raiz' or args.calc == 'log'):
        print("No existe esa función")
        os._exit(0)

    print("PID Proceso padre: %d" % os.getpid())
    with open(args.inputfile, "r") as inputfile:
        for linea in inputfile:
            matriz.append(linea[:-1].split(' '))

    pul = mp.Pool(processes = int(args.process))

    results=[]
    results = pul.map_async(func_calc,matriz).get()
    print("WAIT")
    for linea in results:
        print(linea)

def func_calc(linea):
    global args
    if len(linea)>4:
        time.sleep(3)
        calc = []
    if args.calc == 'pot':
        for element in linea:
            calc.append(math.pow(int(element), int(element)))
        print(calc)
    elif args.calc == 'raiz':
        for element in linea:
            calc.append(math.sqrt(int(element)))
        print(calc)
    elif args.calc == 'log':
        for element in linea:
            calc.append(math.log10(int(element)))
        print(calc)
    print("PID Proceso padre desde hijo: %d" % os.getppid())
    return calc

if __name__ == '__main__':
    main()