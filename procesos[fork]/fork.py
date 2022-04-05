import argparse
import os 
parser = argparse.ArgumentParser()


parser.add_argument('-n',type=int,help='python3 ')
parser.add_argument('-help',type=str, help ='python3 fork.py -n num or -v num')
parser.add_argument('-v',type=str, help= 'modo verbose')

args = parser.parse_args()


    
if __name__ == "__main__":
 
    print ('inicio del proceso padre')
    if args.n == '-n':
        i = args.n
    else :
        i = args.v

        fpid = os.fork() # La ejecución está completa, i = 0, fpid = 0
        if fpid > 0 and i == args.n:
            print("PID=", os.getpid() + "PPID=", os.getppid())
            print(" \n", fpid)

        if fpid > 0 and i == args.v:
            print("Inicio proceso hijo. %d parent %4d %4d ",os.getpid (), os.getppid ())
        
        if fpid == 0:
            print("%d child  %4d %4d %4d" % (i, os.getppid(), os.getpid(), fpid))
        else:
            print("%d parent %4d %4d %4d" % (i, os.getppid(), os.getpid(), fpid))




