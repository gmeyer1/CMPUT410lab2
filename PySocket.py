# CMPUT 410 - Winter 2015
# Glenn Meyer
# gmeyer1
# Code modified from example in tutorial given to us in labs
# http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys

try:
    import thread
except ImportError:
    import _thread as thread
 
HOST = ''
PORT = 8888
 
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message: ' + msg[1])
    sys.exit()
    
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n')
     
    while True:
         
        data = conn.recv(1024)
        reply = 'Hello ' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    conn.close()
 
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    thread.start_new_thread(clientthread ,(conn,))
 
s.close()
