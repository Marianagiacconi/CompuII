import os, sys
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', required= True)
    args = parser.parse_args()


    r, w = os.pipe() 
    
    processid = os.fork()
    if processid:
        w = os.fdopen(w, 'w')
        w.write("Hola Mundo")
        w.write("\n que tal")
        sys.exit(0)
    
    else:
        # This is the child process
        os.close(w)
        r = os.fdopen(r)
        str = r.read()
        print(str)
        print (str[::-1])
        r.close()
        sys.exit(0)

if '__main__' == __name__:
    
    main()