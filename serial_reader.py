import platform
import serial
from serial.tools import list_ports
from time import sleep

# Define default ports for each OS
macos_ports = ['/dev/tty.usbmodem2101']
linux_ports = ['/dev/ttyUSB0']
windows_ports = ['COM3', 'COM4']  # add more if needed

# Select candidate ports based on operating system
system = platform.system()
if system == 'Darwin':
    candidate_ports = macos_ports
elif system == 'Linux':
    candidate_ports = linux_ports
elif system == 'Windows':
    candidate_ports = windows_ports
else:
    candidate_ports = macos_ports

# Try to open each port until one succeeds
ser = None
for port in candidate_ports:
    try:
        ser = serial.Serial(port, 9600, timeout=1)
        break
    except serial.SerialException:
        continue

if ser is None:
    print("Unable to open any default serial ports:")
    for p in candidate_ports:
        print(f"  {p}")
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
