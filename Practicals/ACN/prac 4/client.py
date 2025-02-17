import socket

def run_client():
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            # Get user input
            message = input("Enter message (type 'bye' to quit): ")
            if message.lower() == 'bye':
                break
            # Send the message to the server
            s.sendall(message.encode('utf-8'))
            # Wait for the server's response and decode it
            data = s.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")
    print("Client closed.")

if __name__ == '__main__':
    run_client()
