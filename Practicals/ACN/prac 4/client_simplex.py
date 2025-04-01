import socket

def run_simplex_client():
    HOST = '192.168.49.245' #simple loopback address change it to your server's ip address
    PORT = 65432 # Random port to run the client

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
        print("[Simplex Client] Received:", data.decode('utf-8'))

if __name__ == '__main__':
    run_simplex_client()
