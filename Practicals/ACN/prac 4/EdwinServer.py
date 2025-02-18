import socket

# Create a TCP socket
s=socket.socket()

# Bind to a specific IP and Port
s.bind(("192.168.137.72", 65434))

# Listen for incoming connections
s.listen(1)
print("Server listening on port 123")

# Accept client connection
client_socket, client_address = s.accept()
print(f"Connection from {client_address} established.")

# Receive data from client
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

# Send response to client
client_socket.send("Take me to church!".encode())

# Close connections
client_socket.close()
s.close()