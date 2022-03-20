import argparse
from genericpath import exists
from hashlib import new
from pathlib import Path
from click import argument

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, help='existente.txt')
parser.add_argument('-o', type=str, help='nuevo.txt')

args = parser.parse_args()

class leerArchivo ():
    def exists():
        a = Path('.txt').exists()
        if a == True:
            f = open ('ej2/existente.txt','r')
            mensaje = f.read()
            print(mensaje)
            f.close()
        return mensaje
    def new():
        a = Path('.txt').exists()
        if a == False:
            with open('ej2/nuevo.txt','r+') as myfile:
                data = myfile.read()
                myfile.seek(0)
                myfile.write('Hola new')
                myfile.truncate()
                print(myfile)
            return data

if __name__ == "__main__":
    i = input('escriba -i para ver si existe un archivo, o -o para sobrescribir el existente: ')
    if i == '-i':
        leerArchivo()
        print(exists)
    if i =='-o':
        leerArchivo()
        print(new)