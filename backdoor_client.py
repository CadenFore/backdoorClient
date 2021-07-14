import socket
srv_addr = input('Server IP address: ')
srv_port = int(input('Server port: '))

def print_menu():
    print('''\n\n0) Close the connection
1) Get system info
2) List directory contents''')

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((srv_addr, srv_port))

print('Connection established')
print_menu()

while 1:
    message = input('\n-Select an option: ')

    if(message == '0'):
        my_sock.sendall(message.encode())
        my_sock.close()
        break

    elif(message == '1'):
        my_sock.sendall(message.encode())
        data = my_sock.recv(1024)
        if not data: break 
        print(data.decode('utf-8'))

    elif(message == '2'):
        path = input('Insert path: ')
        my_sock.sendall(message.encode())
        my_sock.sendall(path.encode())
        data = my_sock.recv(1024)
        data = data.decode('utf-8').split(',')
        print('*'*40)
        for x in data:
            print(x)
        print('*'*40)

    print_menu()