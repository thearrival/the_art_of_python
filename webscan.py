import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print(s)

server = str(input("Target website: "))
port = int(input("Enter the port number"))
ip = socket.gethostbyname(server)
print(ip)

request = "GET / HTTP/1.1 n\Host:"+ ip + "/n/n"

s.connect((server,port))
s.send(request.encode())
result = s.recv(1024)
print(result)
