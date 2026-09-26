import socket

HOST = "127.0.0.1"
PORT = 8765

def run() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Listening on {HOST}:{PORT}")
        conn, address = server.accept()
        with conn:
            print(f"Connection from {address}")
            data = conn.recv(1024)
            message = data.decode("utf-8", errors="replace")
            print(f"Received: {message!r}")
            conn.sendall(b"ACK: message received")

if __name__ == "__main__":
    run()
