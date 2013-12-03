#!/usr/bin/env python

import socket

def main():
    host = "10.59.2.2"
    port = 8888
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    while(True):
        msg, addr = sock.recvfrom(1024)
        print "Got this message:" + msg
        if "falun" in msg.lower():
            print "recieved subversive message!!!!!!!!!"

    sock.close()

if __name__ == "__main__":
    main()