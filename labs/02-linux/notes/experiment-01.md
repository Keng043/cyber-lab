# Experiment 01 — Linux identity and system context

## Actual lab result

- User: `kongkiat` (UID 1000)
- Groups include `sudo`, but the shell is not running as root.
- Kernel: WSL2 Linux `6.6.87.2-microsoft-standard-WSL2`.
- Loopback: `127.0.0.1`.

## Permission observation

A new file started as `-rw-r--r--` and changed to `-rw-------` after `chmod 600`.
That means the owner retained read/write access while group and other users lost access.

## Security lesson

Before doing security work, identify the account and system you are operating on. Least privilege reduces the impact of mistakes and limits what a compromised process can access.
