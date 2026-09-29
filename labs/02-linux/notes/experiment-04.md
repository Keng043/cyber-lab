# Experiment 04 — Process and service investigation

## Actual lab result

`ss -ltnp` showed TCP listeners on port 53 bound to `10.255.255.254`, `127.0.0.53`, and `127.0.0.54`. Process ownership was not shown without elevated privileges.

`ps -ef` showed system processes such as PID 1 and systemd-related processes owned by `root`.

## Security lesson

A useful first-pass review connects three things: the listening socket, the process providing it, and the account that owns that process. If ownership cannot be established without elevation, record that limitation rather than bypassing it.
