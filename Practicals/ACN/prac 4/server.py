import socket

def run_server():
    HOST = '127.0.0.1'  # Localhost
    PORT = 65432        # Non-privileged port

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        # Wait for a connection
        conn, addr = s.accept()
        with conn:
            print(f"client {addr} Connected.")
            while True:
                data = conn.recv(1024)
                if not data:
                    break  # No more data: client closed connection
                print(f"Received from client: {data.decode('utf-8')}")
                # Echo the received data back to the client
                conn.sendall(data)

    print("Server closed.")

if __name__ == '__main__':
    run_server()
