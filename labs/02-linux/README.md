# Lab 02 — Linux Foundations

## Objective

Build practical Linux skills used in cybersecurity: identity, permissions, processes, networking, and basic service inspection.

## Environment

- WSL2
- Ubuntu
- Commands are run inside a local lab only

## Exercise 1 — Identity and system context

Run:

```bash
id
whoami
uname -a
pwd
```

Record what each command tells you in `notes/experiment-01.md`.

## Exercise 2 — Files and permissions

Create a temporary lab file, inspect it, then change its permissions:

```bash
touch /tmp/cyber-lab-permissions.txt
ls -l /tmp/cyber-lab-permissions.txt
chmod 600 /tmp/cyber-lab-permissions.txt
ls -l /tmp/cyber-lab-permissions.txt
rm /tmp/cyber-lab-permissions.txt
```

Focus on the owner, group, and read/write/execute bits.

## Exercise 3 — Processes

Run:

```bash
ps aux | head
```

Identify the process ID (PID), user, CPU/memory fields, and command.

## Exercise 4 — Local network inspection

Run:

```bash
ip addr
ss -tuln
```

Identify the loopback interface and any listening TCP/UDP sockets. Do not scan systems you do not own or have permission to test.

## Security questions

- Why should normal work use a least-privileged account instead of root?
- What does `chmod 600` allow the file owner to do?
- Why is a listening socket worth investigating during a security review?
- What is the difference between a process and a network service?
