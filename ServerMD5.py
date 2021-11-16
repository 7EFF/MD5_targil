import socket
import select
import time
import threading
import queue


MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = '0.0.0.0'

print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Listening for clients...")
client_sockets=[]

def socket_work(socket,number,queue,client_address):
    encryp = "Not found"
    while encryp =="Not found" and queue.full():
        socket.send(number.encode())
        min = queue.pop(0)
        #print(min)
        socket.send(str(min).encode())
        req = socket.recv(1024).decode()
        print(client_address, " ", req)
        if req == "Ready for work":
            encryp = socket.recv(1024).decode()
            #print(encryp)
            if encryp != "Not found":
                print("the encypted number is: ", encryp)
                queue.clear()
                return



def send_to(thread, socket):
    thread.acquire()
    socket.send(thread.encode())
    thread.lock()


def main():
    count_client = 0
    queue = []
    for i in range(0, 999999999, 1000000):
        queue.append(i)
    number = input("Enter a number you want to decrypt")
    while True:
        rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])
        for current_socket in rlist:
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(connection)
                #for socket in client_sockets:
                    #socket_work(socket, number, queue, client_address)
                x = threading.Thread(target=socket_work, args=(connection,number,queue,client_address))
                x.start()


if __name__ == '__main__':
    main()

