import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        flag = False
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'quit':
                break

            if msg == 'echo' and flag == False:
                flag = True
            elif msg == 'echo' and flag == True:
                flag = False

            if flag:
                self.csocket.send(bytes(msg, 'UTF-8'))
            else:
                self.csocket.send(bytes("Comandos: echo / quit", 'UTF-8'))
            print("From client:", msg)

        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
