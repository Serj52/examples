import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port)) # подключаемся к серверу
d = s.recv(1024)
print(d.decode())
d = s.send('1'.encode())
b = s.recv(1024)
print(b.decode())
s.close()