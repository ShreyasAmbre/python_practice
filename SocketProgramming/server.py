# Note :- we are creating TCP network which is connection oriented network which require ip address and port
# ip address of client which will request to server for the reponse
import socket

# Note:- To connect to clients we need to create Socket first
s = socket.socket()
print("Socket Created")

# below statement will accept the ip address of client but here server and client are from same machine we use
#  localhost as ip address, Note :-  another is port number used free port number ranger form 0 to 65535
# should select above the 1000 port number till 1000 port are busy with O.S and Machine
s.bind(("localhost", 9999))

# How many client we want to connect at a time?
s.listen(3)
print("Waiting for connection...")

# As we know their r 3 client so we should make a loop  which will accept the connection for incoming clients
# a.accept() will give as client socket and address of client
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()

    print("Connection with", addr, name)
    # In response after connecting server will send below msg to client using client socket store in c
    c.send(bytes("Welcome to Socket Programming", "utf-8"))

    c.close()






