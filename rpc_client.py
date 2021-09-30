# TODO: import socket library
import socket
import sys
import random
NUM_TRANSMISSIONS=10
if (len(sys.argv) > 3) or len(sys.argv) < 2:                                    
  print("Usage: python3 "  + sys.argv[0] + " server_port [random_seed]")        
  sys.exit(1)                                                                   
                                                                                
if len(sys.argv) == 3:                                                          
    random_seed = int(sys.argv[2])                                              
    random.seed(random_seed) 

server_port = int(sys.argv[1])

# TODO: Create a datagram socket for the client
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    # Create an RPC request to compute if a number is prime
    rpc_data = "prime(" + str(random.randint(0, 100)) + ")"
    # TODO: Send RPC request (i.e., rpc_data) to the server
    clientSock.sendto(bytes(rpc_data, "utf-8"), (socket.gethostname(), server_port))
    # Print debugging information
    print("sent: " + rpc_data)
    # TODO: Receive result back from the server into the variable result_data
    result, serveraddr = clientSock.recvfrom(3)
    # TODO: Display it in the format "prime: yes" or "prime: no"
    print("prime: " + result.decode("utf-8") + "\n")

# TODO: Close any sockets that are open
clientSock.close()
