# Experiment 03 — Users, groups, and privilege boundaries

## Actual lab result

- `kongkiat` is UID 1000 with home `/home/kongkiat` and shell `/bin/bash`.
- `kongkiat` belongs to the `sudo` group.
- `sudo -n -l` reported `a password is required`, so no password or elevation was attempted.

## Security lesson

Membership in an administrative group is different from currently running as root. The lab shell remained a normal user shell. Avoid entering credentials into automated security experiments and use the minimum privilege needed.
