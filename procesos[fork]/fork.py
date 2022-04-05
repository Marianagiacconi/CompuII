import argparse
import os 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help='int',action='store')
    parser.add_argument('--h',type=str, help ='python3 fork.py -n num or -v num')
    parser.add_argument('-v',type=int, help= 'modo verbose',action='store')
    args = parser.parse_args()
    #modo num
    if args.n:
        n= os.fork()
        print(f"\n", os.getpid(), '-', os.getppid())

    if args.v:
        #modo verbose    
        v= os.fork()
        print(f"\n Inicio proceso hijo. ",os.getpid ())
        print(f"\n Inicio proceso padre. ",os.getppid ())
    


if __name__ == "__main__":

    main()
