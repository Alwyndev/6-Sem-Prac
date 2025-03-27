import socket
import threading

def handle_client_recv(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"\n[Full-Duplex Server] Received from client: {data.decode('utf-8')}")
        except Exception:
            break

def handle_client_send(conn):
    while True:
        message = input("[Full-Duplex Server] Enter message to send (or 'bye' to quit): ")
        if message.lower() == 'bye':
            conn.sendall(message.encode('utf-8'))
            conn.close()
            break
        conn.sendall(message.encode('utf-8'))

def run_full_duplex_server():
    HOST = '192.168.137.72'
    PORT = 65434  # Different port for full-duplex

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"[Full-Duplex Server] Listening on {HOST}:{PORT}")
        conn, addr = server.accept()
        print(f"[Full-Duplex Server] Connected by {addr}")

        # Start threads for simultaneous send and receive
        recv_thread = threading.Thread(target=handle_client_recv, args=(conn,))
        send_thread = threading.Thread(target=handle_client_send, args=(conn,))
        recv_thread.start()
        send_thread.start()
        recv_thread.join()
        send_thread.join()
    print("[Full-Duplex Server] Server closed.")

if __name__ == '__main__':
    run_full_duplex_server()
