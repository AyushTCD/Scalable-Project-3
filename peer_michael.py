import socket
import sys
import threading

source_port = 33300
dest_port = 33301
other_ip = "10.35.70.1"

print("punching hole")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('0.0.0.0', source_port))
sock.sendto(b'0', (other_ip, dest_port))

print("Ready to exchange messages")


def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', source_port))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n'.format(data.decode()), end = '')
    
listener = threading.Thread(target=listen, daemon=True)
listener.start()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', dest_port))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (other_ip,dest_port))

