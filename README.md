# Cli53_backups

A small Python script that backs up Amazon **Route 53** DNS zones with [`cli53`](https://github.com/barnybug/cli53).
It creates a folder named with today's date and exports each zone to a text file inside it.

> **Resumen:** script que exporta zonas DNS de Route 53 con `cli53` a una carpeta con la fecha del día.

## How it works

`backupdns_ver1.py`:

1. Creates `<backup folder>/<YYYYMMDD>`.
2. Runs `cli53 export <zone>` once per zone and saves the output as `<zone>.txt`.
3. Prints `Backup is done!`.

## Setup

- Install `cli53` and configure your AWS credentials as `cli53` expects (environment variables or `~/.aws`).
- Edit the script: set the destination folder and replace `dns1.txt` ... `dns6.txt` with your own zone names.
- It is written for **Python 2**. To run it on Python 3, change the `print` statement to a function and write the
  folder mode as `0o755`.

## Run

```bash
python2 backupdns_ver1.py
```

Schedule it with `cron` for a daily backup, for example `0 2 * * * python2 /path/backupdns_ver1.py`.

Licence: The Unlicense.
