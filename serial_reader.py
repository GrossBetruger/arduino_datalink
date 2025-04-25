#!/usr/bin/env python3
"""
Script to write to or read from Arduino serial port.

Modes:
  --write : prompt for message and send to Arduino
  --read  : continuously read lines from Arduino and log to arduino_log.txt
"""
import argparse
import platform
import serial
from serial.tools import list_ports
from time import sleep
import sys


THRESHOLD = 1

# Default serial port discovery
def get_serial_port(baudrate=9600, timeout=1):
    """Attempt to open a serial port from OS-specific candidates."""
    macos_ports = ['/dev/tty.usbmodem2101']
    linux_ports = ['/dev/ttyUSB0']
    windows_ports = ['COM3', 'COM4']
    system = platform.system()
    if system == 'Darwin':
        candidates = macos_ports
    elif system == 'Linux':
        candidates = linux_ports
    elif system == 'Windows':
        candidates = windows_ports
    else:
        candidates = macos_ports

    for port in candidates:
        try:
            ser = serial.Serial(port, baudrate, timeout=timeout)
            print(f"Opened serial port: {port}")
            sleep(2)
            return ser
        except serial.SerialException:
            continue

    print("Unable to open any default serial ports:")
    for p in candidates:
        print(f"  {p}")
    print("Available ports:")
    for p in list_ports.comports():
        print(f"  {p.device}")
    sys.exit(1)

def write_mode(ser):
    """Prompt the user and write a single message to the serial port."""
    msg = input("Enter a message: ")
    handshake = b'\x00\x01' * 4
    ser.write(handshake)
    ser.write(msg.encode('utf-8'))
    print(f"Sent: {msg}")

def read_mode(ser, outfile='arduino_log.txt'):
    """Continuously read integer lines from the serial port and log to file."""
    buf = []
    handshake = False
    try:
        with open(outfile, 'w') as f:
            while True:
                line = ser.readline().strip()
                if not line:
                    continue
                try:
                    data = int(line)
                    data = 1 if data > THRESHOLD else 0
                    buf.append(data)
                    if handshake is False and buf[-8:] == [1] * 8:
                        handshake = True
                        buf = []

                    if handshake is False:
                        continue

                    buf.append(data)
                    if 1 in buf and buf[-8:] == [0] * 8:
                        print("end signal: ", buf)
                        break
                except ValueError:
                    continue
                f.write(f"{data}\n")
                f.flush()
    except KeyboardInterrupt:
        print("\nData capture stopped.")

def main():
    parser = argparse.ArgumentParser(
        description="Arduino serial read/write utility"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--read', action='store_true',
        help='Read from serial port and log to arduino_log.txt'
    )
    group.add_argument(
        '--write', action='store_true',
        help='Write a message to serial port'
    )
    args = parser.parse_args()
    ser = get_serial_port()
    if args.write:
        write_mode(ser)
    elif args.read:
        read_mode(ser)

if __name__ == '__main__':
    main()


# plot the data
