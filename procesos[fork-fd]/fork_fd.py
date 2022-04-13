import argparse
import os 
import time

def main():

    
  
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,help='procesos',action='store')
    parser.add_argument('-r',type=int, help ='letras')
    parser.add_argument('-f', action='store', required= True)
    parser.add_argument('-v', help= 'modo verbose',action='store')
    args = parser.parse_args()

    with open(args.f,'+w') as f:
        for i in range (args.r):
            letras = chr(65 + i)  
            if args.v : 
                args.n = os.fork()
                print(f"\n  Proceso pid ",os.getpid () , 'escribiendo letra', letras)
            else:
                for i in range(args.n):
                    args.n = os.fork()
                    print(f"",letras)
                f.write(letras)
                f.flush()
                time.sleep(i)
            os._exit(0)
        os.wait()

if '__main__' == __name__:
    
    main()