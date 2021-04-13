# DDNS Updater
Python script running as __system service__ which automatically updates a DynDNS in a specified interval via HTTP

## Settings
You can specify the following properties in the script (ddnsupdater.py):
- __interval__ (in minutes)
- __ddns__ (update-url)

## Installation on Raspberry Pi
- Paste **ddnsupdater.py** into **/scripts/**
- Paste **ddnsupdater.service** into **/lib/systemd/system/**

## Commands
Enables auto-restart on reboot
```
sudo systemctl enable ddnsupdater
```
Starts the service
```
sudo service ddnsupdater start
```
Shows the logs
```
sudo service ddnsupdater status
```
Stops the service
```
sudo service ddnsupdater stop
```
