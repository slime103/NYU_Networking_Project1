# TODO: import socket library
import socket
import sys
import random
import string

RAND_STR_LEN = 10


# Function to generate random strings
def rand_str():
    ret = ''
    for i in range(RAND_STR_LEN):
        ret += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    return ret


NUM_TRANSMISSIONS = 10
if (len(sys.argv) > 3) or len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " server_port [random_seed]")
    sys.exit(1)

if len(sys.argv) == 3:
    random_seed = int(sys.argv[2])
    random.seed(random_seed)

server_port = int(sys.argv[1])

# TODO: Create a socket for the server on localhost
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: Bind it to a specific server port supplied on the command line
sock.bind((socket.gethostname(), server_port))
# TODO: Put server's socket in LISTEN mode
sock.listen(1)
# TODO: Call accept to wait for a connection
clientSocket, address = sock.accept()
# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    # TODO: receive data over the socket returned by the accept() method
    rs = clientSocket.recv(10)
    # TODO: print out the received data for debugging
    print("received data: " + rs.decode("utf-8"), end="; ")
    # TODO: Generate a new string of length 10 using rand_str
    rs2 = rand_str()
    print("appended: " + rs2)
    # TODO: Append the string to the buffer received
    concat = rs.decode("utf-8") + rs2
    # TODO: Send the new string back to the client
    clientSocket.send(bytes(concat, "utf-8"))
# TODO: Close all sockets that were created
clientSocket.close()
sock.close()
