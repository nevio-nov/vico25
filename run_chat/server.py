import socket
import threading
import json

HOST = "0.0.0.0"
PORT = 5000

clients = []

def handle_client(conn, addr):
    print(f"Connessione da {addr}")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = json.loads(data.decode())
            print(f"Messaggio da {addr}: {msg}")

            for c in clients:
                if c != conn:
                    try:
                        c.sendall(json.dumps(msg).encode() + b"\n")
                    except:
                        pass
    finally:
        print(f"{addr} disconnesso")
        clients.remove(conn)
        conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print(f"In ascolto su {HOST}:{PORT}")
    while True:
        conn, addr = sock.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
