import socket
import threading
import json
import time
import sys

NODE_NAME = sys.argv[1] if len(sys.argv) > 1 else "node"
HOST = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
PORT = 5000


def receiver(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        for line in data.decode().splitlines():
            msg = json.loads(line)
            print(f"Messaggio ricevuto: {msg}")


with socket.create_connection((HOST, PORT)) as sock:
    threading.Thread(target=receiver, args=(sock,), daemon=True).start()
    print('you are connected to the global chat as:', NODE_NAME)
    while True:

        msg = input()
        msg = "from " + NODE_NAME + ": " + msg
        sock.sendall(json.dumps(msg).encode())
        time.sleep(2)
