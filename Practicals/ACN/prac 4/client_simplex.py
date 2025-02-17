import socket

def run_simplex_client():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
        print("[Simplex Client] Received:", data.decode('utf-8'))

if __name__ == '__main__':
    run_simplex_client()
