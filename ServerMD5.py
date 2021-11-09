import socket
import select
import time
import threading

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = '0.0.0.0'

print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Listening for clients...")
client_sockets = []


def send_to(thread, socket):
    thread.acquire()
    socket.send(thread.encode())
    thread.lock()


def main():
    count_client = 0
    list =[range(0,999999999,1000000)]
    number = input("Enter a number you want to decrypt")
    while True:
        rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(connection)
                req=""

                for socket in client_sockets:
                    socket.send(number.encode())
                    req = socket.recv(1024).decode()
                    print(client_address, " ", req)
                    if req == "Ready for work":
                        encryp = socket.recv(1024).decode()
                        print("the encypted number is: ", encryp)
                        return
                    else:
                        continue



if __name__ == '__main__':
    main()
