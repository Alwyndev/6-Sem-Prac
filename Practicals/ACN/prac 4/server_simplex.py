import socket

def run_simplex_server():
    HOST = '127.0.0.1'
    PORT = 65432  # Use a port above 1023

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[Simplex Server] Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"[Simplex Server] Connected by {addr}")
            message = input("[Simplex Server] Enter message to send: ")
            conn.sendall(message.encode('utf-8'))
            print("[Simplex Server] Message sent, closing connection.")

if __name__ == '__main__':
    run_simplex_server()
