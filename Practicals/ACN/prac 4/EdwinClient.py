import socket
import threading

def receive_messages(client):
    """Receives messages from the server."""
    while True:
        try:
            response = client.recv(1024).decode("utf-8")
            if not response:
                break
            print(f"\nServer: {response}\nClient: ", end="")
        except:
            break
    client.close()

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "192.168.137.245"  # Replace with server's IP
    server_port = 65434  # Replace with server's port

    try:
        client.connect((server_ip, server_port))
        print("Connected to server")

        # Start a thread to listen for incoming messages
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

        while True:
            msg = input("Client: ")
            if msg.lower() == "exit":
                client.send("closed".encode("utf-8"))  # Notify server about closing
                break
            client.send(msg.encode("utf-8")[:1024])

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed.")

run_client()