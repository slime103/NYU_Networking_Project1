# TODO: import socket library
import socket
import sys

NUM_TRANSMISSIONS = 10
if (len(sys.argv) < 2):
    print("Usage: python3 " + sys.argv[0] + " server_port")
    sys.exit(1)
assert (len(sys.argv) == 2)
server_port = int(sys.argv[1])


# function to check if n is prime or not
def is_prime(n):
    if n < 1:
        return "no"
    if n == 1:
        return "yes"
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return "no"

    return "yes"


# TODO: Create a socket for the server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO: Bind it to server_port 
sock.bind((socket.gethostname(), server_port))

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    # TODO: Receive RPC request from client
    rpc_data, clientaddr = sock.recvfrom(10)
    # TODO: Turn byte array that you received from client into a string variable called rpc_data
    rpc_str = rpc_data.decode("utf-8")
    # TODO: Parse rpc_data to get the argument to the RPC.
    # Remember that the RPC request string is of the form prime(NUMBER)
    # print("decoded: " + rpc_str)
    rpc_str = rpc_str[6: len(rpc_data) - 1]
    # TODO: Print out the argument for debugging
    print("argument is " + rpc_str)
    # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)
    result = is_prime(int(rpc_str))
    # TODO: Send the result of primality check back to the client who sent the RPC request
    sock.sendto(bytes(result, "utf-8"), clientaddr)

# TODO: Close server's socket
sock.close()
