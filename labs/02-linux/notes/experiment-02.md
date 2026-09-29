# Experiment 02 — Local process and socket observation

## Process observation

`ps aux` showed processes with a PID, owning user, resource fields, and command. System processes such as PID 1 were owned by `root`, while the lab user was `kongkiat`.

## Network observation

`ip addr show lo` confirmed the loopback interface at `127.0.0.1`.

`ss -tuln` showed DNS-related UDP/TCP listeners on port 53, including loopback addresses. The command only observed local state; it did not scan another machine.

## Security lesson

A process can provide a network service by listening on a socket. During a security review, unexpected listeners deserve investigation because every reachable service adds potential attack surface.
