import sys
import socket
import re
PORT = int(input('Port: '))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((s.getsockname()[0], PORT))
print()
s.listen(5)

running = True
while running:
    clientsocket, adress = s.accept()
    if clientsocket:
        #msg = input("What do you wish to send?: ")
        pass
    print(f"Connection to: {adress}. has been made")
    #clientsocket.send(bytes(f"{msg}", "utf-8"))

    fullevent1 = ''
    fullevent2 = ''
    event = []
    is_event1_full = False
    do = ''

    running_event = ''

    while clientsocket:
        clientres = clientsocket.recv(1024)
        if clientres.decode('utf-8') != '':
            #fullevent1 += clientres.decode('utf-8')
            event.append(clientres.decode('utf-8'))
            if clientres.decode('utf-8').find('\n') > -1:
                fullevent1 += clientres.decode('utf-8')
                is_event1_full = True
            fullevent1 += clientres.decode('utf-8').split('\n')[0]
            if is_event1_full:
                is_event1_full = False
                event.append(fullevent1)
                fullevent1 = ''
                fullevent1 += clientres.decode('utf-8').split('\n')[1]
            #print(fullevent1)
            print(str(event[-1]).split('\n')[0])
            do = str(event[-1]).split('\n')[0]
        
        else:
            clientsocket = None


        if do == 'MAB1':
            if running_event == do:
                print('stopping')
                running_event = ''
            else:
                running_event = do
                print('Moving forward')


        elif do == 'MA1':
            if running_event == do:
                print('stopping')
                running_event = ''
            else:
                running_event = do
                print('MB_speed = 0; MA_speed = 1000')

        elif do == 'MB1':
            if running_event == do:
                print('stopping')
                running_event = ''
            else:
                running_event = do
                print('MA_speed = 0; MB_speed = 1000')

        elif do == 'MAB-1':
            if running_event == do:
                print('stopping')
                running_event = ''
            else:
                running_event = do
                print('Moving backwards')


        
s.close()
