import hashlib
import socket
import select
import time

def main():
    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 5555))
    str2 = input("enter md5 number")
    print("the original number is:", end="")
    i = 0
    while True:
        md = str(i)
        for j in range(len(md), 11):
            md = md.zfill(j)
            # print(md)
            result = hashlib.md5(md.encode())
            if (result.hexdigest() == str2):
                print(md)
                return
        i = i + 1

if __name__ == '__main__':
    main()
