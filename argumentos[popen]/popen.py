import argparse
import os
import subprocess as sp
from sys import stdout
from datetime import datetime

#El código deberá crear los archivos pasados por los argumentos -f y -l en el caso de que no existan.
#El código deberá ejecutar el comando haciendo uso de subprocess.Popen, y almacenar su salida en el archivo pasado en el parámetro -f. 
# En el archivo pasado por el modificador -l deberá almacenar el mensaje “fechayhora: Comando XXXX ejecutado correctamente” o en su defecto el mensaje de error generado por el comando si este falla.
parser = argparse.ArgumentParser()
parser.add_argument('-c', type=str, help="string")
parser.add_argument('-f', type=str, help="string")
parser.add_argument('-l', type=str, help="string") 

args= parser.parse_args()

def op():

    with open (args.outputfile, "ip a") as outputfile:
        outp= sp.Popen(args.command.split(), stdout=sp.PIPE, shell= True)
        out= outp.stdout
        out.write(stdout)

    with open (args.log_file, "ip a") as log_file:
        now = datetime.now()
        sp.Popen(stdout=log_file, stderr=sp.PIPE)
        log_file.write(("Fecha y hora:",now.utcnow()) + 'comando'+ stdout + 'ejecutado correctamente')

if __name__ == '__main__':
    op()
