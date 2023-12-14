import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Loopback address
PORT = 12345

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Store connected clients
clients = []

# Function to handle incoming client connections
def handle_client(client_socket, client_address):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f'[{client_address[0]}:{client_address[1]}]: {message}')
            broadcast_message(message, client_socket)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()

# Function to broadcast a message to all connected clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
                clients.remove(client)
                client.close()

# Accept and handle incoming client connections
print("Server is listening...")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    clients.append(client_socket)
    
    # Create a thread to handle the client's messages
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
