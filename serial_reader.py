import os
import serial
from time import sleep
# Replace 'COM3' with your Arduino’s serial port (e.g., '/dev/ttyUSB0' for Linux)
macos_port = '/dev/tty.usbmodem2101'
linux_port = '/dev/ttyUSB0'

try:
    ser = serial.Serial(macos_port, 9600, timeout=1)
except serial.SerialException:  
    print(f"Serial port not found: {macos_port}")
    # run ls /dev/tty.* to find the correct port and print the output
    print("Available ports:")
    print(os.popen('ls /dev/tty.*').read())
    exit()

# Open (or create) a file to save the serial data
with open('arduino_log.txt', 'w') as f:
    try:
        ser.write(bytes(input("Enter a message: "), 'utf-8'))
        sleep(0.1)
        while True:
            # serial_data = ser.read()
            byte_data = ser.read(2)

            if any(junk in byte_data for junk in [b'\r', b'\n', b'\x00']):
                continue
          
            data = int.from_bytes(byte_data, 'big', signed=False)
            f.write(f"{data}\n")
                
    except KeyboardInterrupt:
        print("Data capture stopped.")


# plot the data
