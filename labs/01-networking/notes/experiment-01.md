# Experiment 01 — Listening Port

## What I tested

I started the local TCP server and checked port 8765 with the probe.

## Result

- Server running: `127.0.0.1:8765 -> OPEN`
- Server stopped: `127.0.0.1:8765 -> CLOSED`

## What this means

A port is not automatically an open door. It becomes reachable when a program is listening there.

The probe only checked whether a TCP connection could be made. It did not identify or attack a service.

## Security lesson

Every listening service increases the number of places that need protection. Keeping this lab on `127.0.0.1` means the service is intended to be reachable only from this computer.
