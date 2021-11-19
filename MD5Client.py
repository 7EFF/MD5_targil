import hashlib
import socket
import select
import threading
import time

class work:
    def __init__(self,min,str2,my_socket,i):
        self.min=min
        self.str2=str2
        self.my_socket=my_socket
        self.i=i
    def Find(self):
        while self.i < self.min + 1000000:
            md = str(self.i)
            for j in range(len(md), 11):
                md = md.zfill(j)
                # print(md)
                result = hashlib.md5(md.encode())
                if (result.hexdigest() == self.str2):
                    print("the original number is:", end="")
                    print(md)
                    self.my_socket.send(md.encode())
                    # time.sleep(0.05)
                    return
            self.i = self.i + 1
        msg = "Not found"
        self.my_socket.send(msg.encode())
        return

def main():
    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 5555))
    while True:
        str2 = my_socket.recv(1024).decode()
        time.sleep(0.1)
        min = int(my_socket.recv(1024).decode())
        #str2 = input("enter md5 number")
        i = min
        print("currently working on: ",min," to ",min+1000000)
        message = "Ready for work"
        my_socket.send(message.encode())
        time.sleep(0.1)
        user = work(min,str2,my_socket,i)
        x = threading.Thread(target=user.Find)
        x.start()

if __name__ == '__main__':
    main()
