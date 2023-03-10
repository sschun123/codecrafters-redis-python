# Uncomment this to pass the first stage
import socket
import threading

class RESP:
    @staticmethod
    def simple_string(str):
        return '+' + str + '\r\n'

def create_client(clientsocket):
    while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            clientsocket.send(RESP.simple_string('PONG').encode())
    clientsocket.close()

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    # Convenience function which creates a SOCK_STREAM type socket bound to *address* (a 2-tuple (host, port)) and return the socket object.
    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket:
        print('waiting for new connection...')
        while True:
            (clientsocket, addr) = server_socket.accept() # wait for client
            print('incoming connection from ', addr)
            client_thread = threading.Thread(target=create_client, args=(clientsocket,))
            client_thread.start()

if __name__ == "__main__":
    main()
