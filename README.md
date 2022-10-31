# RASPI STREAMING
A simple Raspberry Pi streaming service.

# USAGE
## Step 1. Activate Raspberry Pi camera system and update library needed

This is important step. You can follow turtorial [here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera).

## Step 2. Import code to device

There are two way to import code. Clone all repository or copy content of ``pi.py``.

## Step 3. Run local

Simple, type in terminal: ``python3 pi.py``

Now you can visit streaming in browser or tools like VLC. Note: Please make sure you have true IP address and port of device.

URL to visit maybe like: http://192.168.1.xyz:8000/stream.mjpg

If you want this script auto run when startup, you can use ``cron``.

## Step 4: Public to internet via ngrok
https://www.sitepoint.com/use-ngrok-test-local-site/




