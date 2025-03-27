import socket

def run_half_duplex_client():
    HOST = '127.0.0.1' #Default loopback host address. Change it to your host/server address.
    PORT = 65433 # Random port to run the client

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = input("[Half-Duplex Client] Enter message (or 'bye' to quit): ")
            if message.lower() == 'bye':
                break
            s.sendall(message.encode('utf-8'))
            data = s.recv(1024)
            print(f"[Half-Duplex Client] Received: {data.decode('utf-8')}")
    print("[Half-Duplex Client] Connection closed.")

if __name__ == '__main__':
    run_half_duplex_client()
