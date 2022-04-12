import argparse
import os 
from pathlib import Path
import random

def main():

    
  
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help='procesos',action='store')
    parser.add_argument('-r',type=str, help ='letras')
    parser.add_argument('-f', action='store_true')
    parser.add_argument('-v',type=str, help= 'modo verbose',action='store')
    args = parser.parse_args()


    if args.f == True:
        f = Path('./compuII/procesos[fork-fd]/fork_fd.py/letras.txt')
        f = open(f)
        
    else:
        f = Path('./compuII/procesos[fork-fd]/fork_fd.py/letras.txt')
        print(f)
        if args.v :
            letras= ['A', 'B', 'C', 'D', 'E']
            let = [letras]
            v = args.n
            args.n = os.fork()
            print(f"\n  Proceso pid ",os.getpid () , 'escribiendo letra', let)
        
        else:
            i = args.n
            args.r = letras= ['A', 'B', 'C', 'D', 'E'] 
            for i in range(len(letras)):
                print(i)
                i = os.fork()


if '__main__' == __name__:
    
    main()


