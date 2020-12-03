import socket
import threading

HEADER = 64
PORT = 5300
SERVER_IP = socket.gethostbyname(socket.gethostname()) #RETURNS STRING
ADDR = (SERVER_IP,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ">>DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def DealWithClient(conn,addr):
    print(f"New connection detected. {addr} is connected.")

    connected = True

    while connected:
        messageLength = conn.recv(HEADER).decode(FORMAT)#HOW MANY BYTES WE PREFER TO LET

        if messageLength:
            messageLength = int(messageLength)
            message = conn.recv(messageLength).decode(FORMAT)
            print(f"{addr} -- {message}")
            if message == DISCONNECT_MESSAGE:
                connected = False
                print("Disconnect request is on process...")

            conn.send("Message received".encode(FORMAT))

    conn.close()
    print("Connection closed.")


def Start():
    server.listen()
    print(f"Listening... {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=DealWithClient, args=(conn,addr)) #CREATİNG A NEW THREAD
        thread.start()
        print(f"Connection is active. Thread: {threading.active_count()-1}")

print("Server is starting...")
Start()

