import threading
import socket

host = '127.0.0.1'  # this is the localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()

clients = []
nicknames = []

# send the following message to all the clients that are in the clients array


def broadcast(message):
    for client in clients:
        client.send(message)

# this function runs a while loop and checks for the client in the array
# and tries to send 1024 bytes of the message, else it finds the index of the client
# removes the client and prints the nickname of the client before removing him from the nicknames array
# and exits the loop


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break
