import socket

HEADER = 64
SERVER_IP = "192.168.80.1" #MATCH WITH SERVER IP
PORT = 5300
ADDR = (SERVER_IP,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ">>DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def SendMessage(message):
    message = message.encode(FORMAT)
    messageLength = len(message)
    sendLength = str(messageLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT))
    
SendMessage("Hello World")
#SendMessage(DISCONNECT_MESSAGE)