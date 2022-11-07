import socket
import argparse
import socketserver



class Server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        parser = argparse.ArgumentParser(description="server")
        parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto")
        parser.add_argument("-c", "--concurrency", type=str, required=True, help="Concurrencia: forking o threading")
        args = parser.parse_args()
        HOST, PORT = "", args.port
        s.listen()
        s.bind((HOST, PORT))
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
        

    
    socketserver.TCPServer.allow_reuse_address = True
