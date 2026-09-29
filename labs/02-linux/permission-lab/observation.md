# Permission Lab — Observation

## Result

The simulated configuration file was first created with mode `644`, then changed to `600`.

- `644`: owner can read/write; group and others can read.
- `600`: owner can read/write; group and others have no permissions.

The value used in the exercise is a fake demo value, not a real credential.

## Security takeaway

When sensitive configuration is stored in a file, its permissions should match the smallest set of users that actually needs access.
