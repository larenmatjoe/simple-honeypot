import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=22
host="localhost" #need to change while running a network
s.bind((host,port))
s.listen()
connection,ip = s.accept()
try:
    c.send(b"Password:")
    data = c.recv(1024)
    c.send(b"Wrong Password")
    c.send(b"Closing connection")
c.close()
s.close()
try:
    print("Connection from IP Address:{}".format(ip))
if len(data)!=0:
    try:
        print("Password Used:{}".format(data))

