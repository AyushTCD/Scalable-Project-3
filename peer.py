import socket
import sys
import threading
import argparse

source_port = 33300
dest_port = 33301
my_ip = socket.gethostbyname(socket.gethostname())

username = input("Enter username: ")
source_port = int(input("Enter port:"))

print("Ready to exchange messages")

def listen():
    while True:
        data = sock.recv(1024)
        print('\npeer: {}\n'.format(data.decode()), end = '')
    

# Reinstantiate socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((my_ip, source_port))

listener = threading.Thread(target=listen, daemon=True)
listener.start()

while True:
    dest_port = int(input("Enter port to send message to:"))
    dest_addr = input("Enter ip address of peer to send message to:")
    msg = input('> ')
    sock.sendto(msg.encode(), (dest_addr,dest_port))

