import sys
import os
import random
import string
#TODO: import socket libraries
import socket

NUM_TRANSMISSIONS=200
if len(sys.argv) < 2:
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a socket for the receiver
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: Connect this socket to the relay at relay_port
sock.connect((socket.gethostname(), relay_port))

# Iterate NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    # TODO: Receive any data relayed from the relay (i.e., any data sent by the sender to the relay)
    data = sock.recv(201)
    # TODO: Print received data
    print("received: " + data.decode("utf-8"))
# TODO: Close any open sockets
sock.close()