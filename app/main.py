# Uncomment this to pass the first stage
import socket
import time

class RESP:
    @staticmethod
    def simple_string(str):
        return '+' + str + '\r\n'


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    # Convenience function which creates a SOCK_STREAM type socket bound to *address* (a 2-tuple (host, port)) and return the socket object.
    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket:
        # skip the initial connection msg
        (clientsocket, addr) = server_socket.accept() # wait for client
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            clientsocket.send(RESP.simple_string('PONG').encode())
        clientsocket.close()

if __name__ == "__main__":
    main()
