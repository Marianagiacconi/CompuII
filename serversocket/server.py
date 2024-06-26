import socket
import argparse
import socketserver, threading
import signal


class MyTCPHandler(socketserver.BaseRequestHandler):
    def Handler():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
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

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="server")
    parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto")
    parser.add_argument("-c", "--concurrency", type=str, required=True, help="Concurrencia: forking o threading")
    args = parser.parse_args()
    HOST, PORT = "localhost", 9999
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    direcciones = socket.getaddrinfo("localhost", 5000, socket.AF_UNSPEC, socket.SOCK_STREAM)
    if args.concurrence == 'p':
        with ForkedTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()
            #server.shutdown()


    if args.concurrence == 't':
        with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()
            #server.shutdown()