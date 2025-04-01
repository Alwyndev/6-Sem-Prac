import socket

# Create a TCP socket
server_socket = socket.socket()

# Bind the socket to an address and port
server_socket.bind(("192.168.21.77", 65434))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port 65434...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Half-Duplex Communication (Alternating Send and Receive)
while True:
    # Receive data from client
    client_data = client_socket.recv(1024).decode()
    if not client_data or client_data.lower() == "exit":
        print("Client disconnected.")
        break
    print(f"Client: {client_data}")

    # Get server response
    server_response = input("Server: ")
    client_socket.send(server_response.encode())

# Close connections
client_socket.close()
server_socket.close()