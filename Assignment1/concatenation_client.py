import sys
import os
import random
import string

RAND_STR_LEN = 10

# TODO: Import socket library



# Random alphanumeric string
def rand_str():
  ret = ''
  for i in range(RAND_STR_LEN):
    ret += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
  return ret

NUM_TRANSMISSIONS=10
def client_socket_setup(server_port):
    # TODO: Create and return the socket for the client

    # TODO:  Connect this socket to the server


def transmit_using_socket(client_socket):
    # Transmit NUM_TRANSMISSIONS number of times
    for i in range(NUM_TRANSMISSIONS):
      # TODO: Generate a random string of length 10 using rand_str function

      # TODO: Send random string to the server

      # TODO: Print data for debugging

      # TODO: Receive concatenated data back from server as a byte array

      # TODO: Print out concatenated data for debugging

      # TODO: Close socket


if __name__ == "__main__":
    if len(sys.argv) > 3 or len(sys.argv) < 2:
      print("Usage: python3 "  + sys.argv[0] + " server_port [random_seed]")
      sys.exit(1)

    if len(sys.argv) == 3:
        random_seed = int(sys.argv[2])
        random.seed(random_seed)

    server_port=int(sys.argv[1])

    client_socket = client_socket_setup(server_port)
    transmit_using_socket(client_socket)
