import platform
import serial
from serial.tools import list_ports
from time import sleep

# Define default ports for each OS
macos_port = '/dev/tty.usbmodem2101'
linux_port = '/dev/ttyUSB0'
windows_port = 'COM3'  # adjust if needed

# Select port based on operating system
system = platform.system()
if system == 'Darwin':
    port = macos_port
elif system == 'Linux':
    port = linux_port
elif system == 'Windows':
    port = windows_port
else:
    port = macos_port

try:
    ser = serial.Serial(port, 9600, timeout=1)
except serial.SerialException:
    print(f"Serial port not found: {port}")
    print("Available ports:")
    for p in list_ports.comports():
        print(p.device)
    exit()

# Open (or create) a file to save the serial data
with open('arduino_log.txt', 'w') as f:
    try:
        ser.write(bytes(input("Enter a message: "), 'utf-8'))
        sleep(0.1)
        while True:
            # serial_data = ser.read()
            byte_data = ser.readline().strip()
            if byte_data == b'':
                continue
            data = int(byte_data)
          
            # data = int.from_bytes(byte_data, 'big', signed=False)
            f.write(f"{data}\n")
                
    except KeyboardInterrupt:
        print("Data capture stopped.")


# plot the data
