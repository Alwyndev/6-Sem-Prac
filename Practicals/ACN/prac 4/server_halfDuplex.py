import socket

def run_half_duplex_server():
    HOST = '192.168.21.77' #Default loopback address. Change it to your(server) address
    PORT = 65433  # Random port for half-duplex (above 1024)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[Half-Duplex Server] Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"[Half-Duplex Server] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                received = data.decode('utf-8')
                print(f"[Half-Duplex Server] Received: {received}")
                print("[Half-Duplex Server] responding...")
                # Respond to the client
                response = input(f"Server received: {received}\nEnter something to send : ")
                conn.sendall(response.encode('utf-8'))
            print("[Half-Duplex Server] Connection closed.")

if __name__ == '__main__':
    run_half_duplex_server()
