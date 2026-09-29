# Permission Lab — Find the Weak Permission

## Scenario

A local application stores a simulated secret configuration file. Your job is to determine which permission state exposes it and then fix the permission.

## Setup

Inside WSL:

```bash
mkdir -p ~/cyber-lab-permission-demo
printf 'API_KEY=DEMO-ONLY-NOT-A-REAL-KEY\n' > ~/cyber-lab-permission-demo/app.conf
chmod 644 ~/cyber-lab-permission-demo/app.conf
ls -l ~/cyber-lab-permission-demo/app.conf
```

## Investigation

1. Read the permission string from `ls -l`.
2. Explain who can read the file under `644`.
3. Change it to owner-only access:

```bash
chmod 600 ~/cyber-lab-permission-demo/app.conf
ls -l ~/cyber-lab-permission-demo/app.conf
```

4. Explain what changed.
5. Remove the demo directory when finished:

```bash
rm -rf ~/cyber-lab-permission-demo
```

## Security lesson

Permissions are part of access control. A file containing a secret should not be readable by users who do not need it. Real credentials should never be placed in this lab.
