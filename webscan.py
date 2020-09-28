import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print(s)

server = "www.facebook.com"
port = 80
ip = socket.gethostbyname(server)
print(ip)

request = "GET / HTTP/1.1 n\Host:"+ ip + "/n/n"

s.connect((server,port))
s.send(request.encode())
result = s.recv(1024)
print(result)
