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

def send_to(thread,socket):
    thread.acquire()
    socket.send(thread.encode())
    thread.lock()

def main():
    number = input("Enter a number you want to decrypt")
    count_client=0
    while True:
        rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(connection)
                count_client = count_client+1
                Length = len(number)
                Length = Length/count_client
                for socket in client_sockets:
                    message = ""
                    count=0
                    for i in number:
                        message.append(i)
                        count = count+1
                        if count ==Length:
                            socket.send(message)
                            message = ""
                            count = 0
                    #thread = threading.Thread(target=send_to(),args=(1,))
                    #thread.lock()
                    #thread.start()


if __name__ == '__main__':
    main()
