# Experiment 03 — Handling Unexpected Input

## What I tested

I sent three controlled payloads to the local TCP service:

- empty input
- unusual bytes (`HELLO` plus null/non-UTF-8 bytes)
- 1,024 bytes of data

I also sent a 1,025-byte payload to verify the server-side size limit.

## Result

- Empty input / no data: `ERROR: receive timeout`
- Unusual bytes: `ACK: message received`
- 1,024 bytes: `ACK: message received`
- 1,025 bytes: `ERROR: message too large`

## What changed

The original server could wait indefinitely for a client that connected but did not send data. The server now has a receive timeout and a maximum message size.

## Security lesson

A server should not blindly trust incoming data. It should set reasonable limits, handle timeouts, and return controlled errors instead of waiting forever or processing unlimited input.

This experiment was performed only against the local lab service on `127.0.0.1`.
