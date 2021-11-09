import hashlib
import socket
import select
import time

def Recieve(my_socket):
    rlist, slist, xlist = select.select([my_socket], [], [], 0.1)
    str2=""
    for s in rlist:
        str2 = s.recv(1024).decode()
    return str2


def main():
    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 5555))
    str2=""
    str2 = my_socket.recv(1024).decode()
    while True:

        #str2 = input("enter md5 number")
        print("the original number is:", end="")
        i = 0
        message = "Ready for work"
        my_socket.send(message.encode())
        while True:
            md = str(i)
            for j in range(len(md), 11):
                md = md.zfill(j)
                #print(md)
                result = hashlib.md5(md.encode())
                if (result.hexdigest() == str2):
                    print(md)
                    my_socket.send(md.encode())
                    #time.sleep(0.05)
                    return
            i = i + 1


if __name__ == '__main__':
    main()
