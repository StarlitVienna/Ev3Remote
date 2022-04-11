import socket
import time
# Turn IP into a input for Ev3
IP = "192.168.15.4"
PORT = int(input('Port: '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

connected = True
while connected:
    #msg = s.recv(1024)
    #print(msg.decode('utf-8'))
    event = input('What do you wish to send?: ')
    s.sendall(bytes(f'{event} \n', 'utf-8'))
    #time.sleep(5)
    #s.sendall(bytes('Love you <3', 'utf-8'))
    #s.shutdown(2)
    #connected = False
