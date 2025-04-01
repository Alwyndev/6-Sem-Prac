import socket

def run_half_duplex_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "192.168.21.78"  # Replace with the server's IP
    server_port = 8000  # Replace with the server's port
    client.connect((server_ip, server_port))
    
    try:
        while True:
            # Client sends a message first
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])
            
            if msg.lower() == "exit":
                break
            
            # Client waits to receive a message from the server
            response = client.recv(1024).decode("utf-8")
            print(f"Received: {response}")
            
            if response.lower() == "closed":
                break
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client.close()
        print("Connection to server closed")

run_half_duplex_client()