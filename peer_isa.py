import socket
import sys
import threading
import argparse

def listen(sport):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', sport))

        while True:
            data = sock.recv(1024)
            print('\rpeer: {}\n'.format(data.decode()), end = '')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nbr1', help='ip address of neighbours of Rover', type=str)
    parser.add_argument('--nbr2', help='ip address of neighbours of Rover', type=str)
    parser.add_argument('--port', help='Port to operate on', type=int)
    args = parser.parse_args()

    if args.nbr1 is None:
        print("Please specify first neighbour")
        #exit(1)

    if args.nbr2 is None:
        print("Please specify second neighbour")
        #exit(1)

    if args.port is None:
        print("Please specify the port")
        #exit(1)

    
    source_port = 33301
    dest_port = 33300
    other_ip = '0.0.0.0'

    print("punching hole")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('0.0.0.0', source_port))
    sock.sendto(b'0', (other_ip, dest_port))

    print("Ready to exchange messages")

        
    listener = threading.Thread(target=listen, args=source_port, daemon=True)
    listener.start()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', dest_port))

    while True:
        msg = input('> ')
        sock.sendto(msg.encode(), (other_ip,dest_port))

if __name__ == '__main__':
    main()

