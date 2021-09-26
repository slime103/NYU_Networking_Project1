import sys
import os
import random
import string
#TODO: import socket libraries

NUM_TRANSMISSIONS=200
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " relay_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
relay_port=int(sys.argv[1])

# TODO: Create a socket for the receiver

# TODO: Connect this socket to the relay at relay_port

# Iterate NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive any data relayed from the relay (i.e., any data sent by the sender to the relay)

  # TODO: Print received data

# TODO: Close any open sockets
