import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument('-n','--numero',type=int,help='int',action='store')
parser.add_argument('-help',type=str, help ='python3 fork.py -n num or -v num')
parser.add_argument('-v','--verbose',type=int, help= 'modo verbose',action='store')
argsn = parser.parse_args
argsv= parser.parse_args


def main():
    #modo num
        n= os.fork()
        print(f"PID=", os.getpid())
        print(f"PPID=", os.getppid())
        #modo verbose    
        v= os.fork()
        print(f"Inicio proceso hijo. ",os.getpid ())
        print(f"Inicio proceso padre. ",os.getppid ())
    


if __name__ == "__main__":

    main()
