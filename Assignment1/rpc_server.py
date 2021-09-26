#TODO: import socket library
import sys
NUM_TRANSMISSIONS=10
if(len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port = int(sys.argv[1])

# TODO: Create a socket for the server

# TODO: Bind it to server_port 

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # TODO: Receive RPC request from client

  # TODO: Turn byte array that you received from client into a string variable called rpc_data

  # TODO: Parse rpc_data to get the argument to the RPC.
  # Remember that the RPC request string is of the form prime(NUMBER)

  # TODO: Print out the argument for debugging

  # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)

  # TODO: Send the result of primality check back to the client who sent the RPC request

# TODO: Close server's socket
