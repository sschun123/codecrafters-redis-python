# Uncomment this to pass the first stage
import socket

class RESP:
    @staticmethod
    def simple_string(str):
        return '+' + str + '\r\n'


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    # Convenience function which creates a SOCK_STREAM type socket bound to *address* (a 2-tuple (host, port)) and return the socket object.
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        (clientsocket, addr) = server_socket.accept() # wait for client
        clientsocket.send(RESP.simple_string('PONG').encode())
        clientsocket.close()

if __name__ == "__main__":
    main()
