import socket
import time
HOST = '127.0.0.1'  
PORT = 3421       
TEMINAL = "\n*"

msg = "Since mid-May, Uber has required drivers to take selfies to verify they are wearing a mask or face covering before they are able to pick up riders. [SEP] Since when Uber drivers have to wear a mask?" + TEMINAL

msg2 = "Since mid-May, Uber has required drivers to take selfies to verify they are wearing a mask or face covering before they are able to pick up riders. [SEP] What should Uber drivers have to wear?" + TEMINAL

msg3 = "Since mid-May, Uber has required drivers to take selfies to verify they are wearing a mask or face covering before they are able to pick up riders. [SEP] Who is recommended to take a selfies?" + TEMINAL

msg4 = "Soon, certain riders will also be required to take a selfie prior to ordering a ride. [SEP] Who is required to take a photo of themselves?" + TEMINAL

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(msg.encode())
print(client_socket.recv(1024).decode())
client_socket.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(msg2.encode())
print(client_socket.recv(1024).decode())
client_socket.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(msg3.encode())
print(client_socket.recv(1024).decode())
client_socket.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall(msg4.encode())
print(client_socket.recv(1024).decode())
client_socket.close()