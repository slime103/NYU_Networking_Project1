import sys
# TODO: import socket libraries
import socket

NUM_TRANSMISSIONS = 200
if len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " relay_port")
    sys.exit(1)
assert (len(sys.argv) == 2)
relay_port = int(sys.argv[1])


# TODO: Create a relay socket to listen on relay_port for new connections
relay_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: Bind the relay's socket to relay_port
relay_sock.bind((socket.gethostname(), relay_port))
# TODO: Put relay's socket in LISTEN mode
relay_sock.listen(2)
# TODO: Accept a connection first from sender.py (accept1)
senderSocket, senderaddr = relay_sock.accept()
# TODO: Then, accept a connection from receiver.py (accept2)
receiverSocket, receiveraddr = relay_sock.accept()
# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    # TODO: Receive data from sender socket (the return value of accept1)
    # Be careful with the length of data you receive
    data = senderSocket.recv(201)
    # TODO: Check for any bad words and replace them with the good words
    # Replace 'virus' with 'groot'
    # Replace 'worm' with 'hulk'
    # Replace 'malware' with 'ironman'
    decoded = data.decode("utf-8")
    decoded.replace("virus", "groot")
    decoded.replace("worm", "hulk")
    decoded.replace("malware", "ironman")

    # TODO: and forward the new string to the receiver socket (the return value of accept2)
    receiverSocket.send(bytes(decoded, "utf-8"))
    # TODO: print data that was relayed
    print("relayed: " + decoded)
# TODO: Close all open sockets
relay_sock.close()
senderSocket.close()
receiverSocket.close()
