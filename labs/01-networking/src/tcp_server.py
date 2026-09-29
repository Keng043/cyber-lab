import socket

HOST = "127.0.0.1"
PORT = 8765
READ_TIMEOUT = 2.0
MAX_MESSAGE = 1024

def run() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Listening on {HOST}:{PORT}")
        while True:
            conn, address = server.accept()
            with conn:
                print(f"Connection from {address}")
                conn.settimeout(READ_TIMEOUT)
                try:
                    data = conn.recv(MAX_MESSAGE + 1)
                except socket.timeout:
                    conn.sendall(b"ERROR: receive timeout")
                    continue

                if not data:
                    conn.sendall(b"ERROR: empty message")
                    continue

                if len(data) > MAX_MESSAGE:
                    conn.sendall(b"ERROR: message too large")
                    continue

                message = data.decode("utf-8", errors="replace")
                print(f"Received: {message!r}")
                conn.sendall(b"ACK: message received")

if __name__ == "__main__":
    run()
