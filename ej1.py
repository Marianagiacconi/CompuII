import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o',
                    type=str,
                    choices=['+', '-', '*','/'],
                    default='', required=False,
                    help='Operación a realizar con a y b')
parser.add_argument('-n', type=int, help='numero1')
parser.add_argument('-m', type=int, help='numero2')

args = parser.parse_args()

class calculadora():
    
    a = args.n
    b = args.m

    if args.o == '+':
        print(a + b)
    elif  args.o == '-':
        print(a - b)
    elif args.o == '/':
        print(a / b)
    elif args.o == '*':
        print(a * b)
        
if __name__ == "__main__":
    calculadora()