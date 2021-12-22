import socket
import sqlite3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))

conn = sqlite3.connect('dates.db')
conn.execute('CREATE TABLE COMPANY' 
             ' (ID INT PRIMARY KEY NOT NULL,' 
             ' NAME TEXT NOT NULL,'
             ' AGE INT NOT NULL);')
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE)" 
             "VALUES (1, 'Paul', 32)")
conn.commit()
s.listen(5)
while True:
    con, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    con.send('Thank you for the connection'.encode())
    d = con.recv(1024)
    res = conn.execute('SELECT NAME FROM COMPANY WHERE ID = :ID', {'ID': d.decode()}).fetchone()
    print(res)
    con.send(str(res).encode())
    con.close()