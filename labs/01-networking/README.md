# Lab 01 — Networking Foundations

## Objective

Understand TCP from both sides: server bind/listen, client connect, request/response, and shutdown.

## Environment

- Python 3.10+
- localhost (`127.0.0.1`)
- TCP port `8765`

## Exercise

1. Start `src/tcp_server.py`.
2. In another terminal run `src/tcp_client.py`.
3. Observe the connection and response.
4. Change the client message and repeat.
5. In a third terminal run `src/port_probe.py` while the server is running.
6. Stop the server and run the probe again.
7. Record the difference in `notes/experiment-01.md`.

## Security observations

- A listening port exposes a network service.
- Binding to `127.0.0.1` keeps this lab local.
- Real services should validate input and handle malformed requests.
- Sensitive traffic should use authentication and encryption.

## Questions

- What is the difference between a listening socket and an established connection?
- Why is localhost safer for this exercise than `0.0.0.0`?
- What changes when a service listens on all interfaces?
