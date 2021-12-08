import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER, PORT))
except:
    print("Unavailable Server. Sorry!")
    client.close()
else:
    client.sendall(bytes("Client is here", 'UTF-8'))
    while True:
        in_data = client.recv(1024)
        print("From Server :", in_data.decode())
        out_data = input()
        client.sendall(bytes(out_data, 'UTF-8'))
        if out_data == 'quit':
            break
    client.close()
