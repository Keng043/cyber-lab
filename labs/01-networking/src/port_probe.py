import socket

HOST = "127.0.0.1"
PORT = 8765
TIMEOUT = 1.0


def check_port(host: str = HOST, port: int = PORT) -> bool:
    """Return True when a TCP service accepts a connection."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.settimeout(TIMEOUT)
        return probe.connect_ex((host, port)) == 0


def run() -> None:
    state = "OPEN" if check_port() else "CLOSED"
    print(f"{HOST}:{PORT} -> {state}")


if __name__ == "__main__":
    run()
