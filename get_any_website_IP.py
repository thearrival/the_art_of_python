#script written by ismail 


#socket is python module resposible for creating a connection between a clinet and server
import socket

#for activation.. AF_INET stands for IPv4, SOCK_STREAM = TCP protocol 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)


#Input the website 
server = input("Input the name of the website: ")


#get the Ip address.
server_ip = socket.gethostbyname(server)
print(server_ip)
