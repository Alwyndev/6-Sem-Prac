import socket
import threading

def receive_messages(client):
    try:
        while True:
            response = client.recv(1024).decode("utf-8")
            if not response or response.lower() == "closed":
                print("Connection closed by server.")
                break
            print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def run_full_duplex_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "192.168.21.78"  # Replace with the server's IP
    server_port = 8000  # Replace with the server's port
    client.connect((server_ip, server_port))
    
    # Start a separate thread to listen for incoming messages
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    
    try:
        while True:
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])
            
            if msg.lower() == "exit":
                break
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client.close()
        print("Connection to server closed")

run_full_duplex_client()
