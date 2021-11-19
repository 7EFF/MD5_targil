import socket
import select
import threading
import time

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = '0.0.0.0'

print("Setting up server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
print("Listening for clients...")
client_sockets=[]
class server:
    def __init__(self,socket,number,queue,client_address):
        self.socket=socket
        self.number=number
        self.queue=queue
        self.client_address=client_address

    def socket_work(self):
        encryp = "Not found"
        while encryp =="Not found" and len(self.queue)!=0:
            self.socket.send(self.number.encode())
            min = self.queue.pop(0)
            self.socket.send(str(min).encode())
            req = self.socket.recv(1024).decode()
            print(self.client_address, " ", req)
            if req == "Ready for work":
                encryp = self.socket.recv(1024).decode()
                if encryp != "Not found":
                    print("the encypted number is: ", encryp)
                    self.queue.clear()
        return


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
                user = server(connection,number,queue,client_address)
                x = threading.Thread(target=user.socket_work)
                x.start()


if __name__ == '__main__':
    main()

