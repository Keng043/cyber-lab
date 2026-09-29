import socket

HOST = "127.0.0.1"
PORT = 8765
TIMEOUT = 1.0


def probe_service(host: str = HOST, port: int = PORT) -> str:
    """Connect to the lab service and return its first response."""
    with socket.create_connection((host, port), timeout=TIMEOUT) as client:
        client.sendall(b"HELLO\n")
        response = client.recv(1024)
    return response.decode("utf-8", errors="replace")


def run() -> None:
    print(f"{HOST}:{PORT} -> {probe_service()}")


if __name__ == "__main__":
    run()
