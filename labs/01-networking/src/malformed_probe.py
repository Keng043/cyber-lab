import socket

HOST = "127.0.0.1"
PORT = 8765
TIMEOUT = 3.0
MAX_MESSAGE = 1024


def send_payload(payload: bytes, host: str = HOST, port: int = PORT) -> str:
    """Send controlled test data to the local lab service."""
    if len(payload) > MAX_MESSAGE:
        raise ValueError(f"payload exceeds {MAX_MESSAGE} bytes")

    with socket.create_connection((host, port), timeout=TIMEOUT) as client:
        client.sendall(payload)
        response = client.recv(1024)
    return response.decode("utf-8", errors="replace")


def run() -> None:
    payloads = [b"", b"HELLO\x00\xff", b"A" * 1024]
    for payload in payloads:
        try:
            response = send_payload(payload)
            print(f"payload={len(payload):4} bytes -> {response!r}")
        except (OSError, ValueError) as exc:
            print(f"payload={len(payload):4} bytes -> rejected: {exc}")


if __name__ == "__main__":
    run()
