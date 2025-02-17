import socket
import threading

def recv_from_server(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"\n[Full-Duplex Client] Received from server: {data.decode('utf-8')}")
        except Exception:
            break

def send_to_server(sock):
    while True:
        message = input("[Full-Duplex Client] Enter message to send (or 'bye' to quit): ")
        if message.lower() == 'bye':
            sock.sendall(message.encode('utf-8'))
            sock.close()
            break
        sock.sendall(message.encode('utf-8'))

def run_full_duplex_client():
    HOST = '127.0.0.1'
    PORT = 65434

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[Full-Duplex Client] Connected to server at {HOST}:{PORT}")

        recv_thread = threading.Thread(target=recv_from_server, args=(s,))
        send_thread = threading.Thread(target=send_to_server, args=(s,))
        recv_thread.start()
        send_thread.start()
        recv_thread.join()
        send_thread.join()
    print("[Full-Duplex Client] Connection closed.")

if __name__ == '__main__':
    run_full_duplex_client()
