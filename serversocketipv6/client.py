import socket 
servidor="localhost"
direcciones = socket.getaddrinfo(servidor, 5000, socket.AF_UNSPEC, 1)

for direccion in direcciones:
    s = socket.socket(direccion[0], direccion[1])
    print("conectando a :", direccion[4])
    s.connect((direccion[4]))
    comandostr = str(input("escriba comando"))
    comando = bytearray(comandostr, encoding='utf-8')
    s.send(comando)
    response = s.recv(2024)
    print(response)
    s.close()