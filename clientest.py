import socket
import time
PORT = int(input('Port: '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))

connected = True
while connected:
    #msg = s.recv(1024)
    #print(msg.decode('utf-8'))
    event = input('What do you wish to send?: ')
    s.sendall(bytes(f'{event} \n', 'utf-8'))
    #time.sleep(5)
    s.sendall(bytes('Love you <3', 'utf-8'))
    #s.shutdown(2)
    #connected = False
