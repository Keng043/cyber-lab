# Experiment 02 — Basic Service Discovery

## What I tested

I connected to the lab's known TCP port and sent a harmless `HELLO` message.

## Result

The service returned:

`ACK: message received`

## What this means

Finding an open port tells us that something is listening. A small, controlled request can reveal how that service responds.

This is the basic idea behind service discovery: learn what is running before deciding how it should be protected.

## Security lesson

Real services may reveal useful information through banners or responses. Exposing unnecessary version or system details can help an attacker understand a target. Services should return only information that clients actually need.

This experiment stayed on `127.0.0.1` and used the lab's own service.
