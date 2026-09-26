import socket

HOST = "127.0.0.1"
PORT = 8765

def run() -> None:
    message = input("Message: ")
    with socket.create_connection((HOST, PORT), timeout=5) as client:
        client.sendall(message.encode("utf-8"))
        response = client.recv(1024)
        print("Server:", response.decode("utf-8", errors="replace"))

if __name__ == "__main__":
    run()
