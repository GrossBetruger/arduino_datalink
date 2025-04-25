# Arduino Data Link

A minimal end-to-end optical data‑link demonstration using an Arduino’s red LED as transmitter and a light-dependent resistor (LDR) on analog pin A5 as receiver. Text messages sent over serial are encoded as light pulses, detected by the LDR via analog sampling, and sent back over serial to the host for logging and plotting via Python.

## Hardware Setup

1. **Power & Ground**
   - Connect Arduino 5 V to the breadboard’s + rail.
   - Connect Arduino GND to the breadboard’s – rail.

2. **LED (Data Out)**
   - Arduino D2 → [220 Ω resistor] → LED anode.
   - LED cathode → GND rail.

3. **LDR (Light Sensor)**
   ```
   +5 V ──[ LDR ]──┬── Arduino A5
                   │
                  [10 kΩ]
                   │
                 GND
   ```

4. **ASCII‑Breadboard Layout**
   ```text
       +5V rail o================================o
                |
         ┌───┐ [ LDR ]
         │   │     |
         └───┘ [10kΩ]
                |
       —————————————————
       - GND rail o================================o

       D2 ── [220Ω] ──|>|── GND rail
   ```
## Circuit Schematic

A schematic diagram of the LED → LDR data link:

```text
  +5V o──[ LDR ]──┬── A5 (Arduino)
                  │
                [10kΩ]
                  │
  GND o───────────┘

  D2 (Arduino) o──[220Ω]──|>|── GND o
```

To generate a plotted schematic, run:

```bash
poetry run python schematic.py
```

## Software Requirements

- Arduino board (e.g., Uno)
- Python 3.13
- Poetry
- pyserial, numpy, pandas, plotly (managed via Poetry)

## Installation

```bash
poetry install
```

## Usage

1. **Find Serial Port**  
   ```bash
   ./find_port.sh
   ```

2. **Configure `serial_reader.py` (if needed)**  
   Update `macos_port`, `linux_port`, or `windows_port` to match your system’s Arduino serial port.

3. **Clear Old Log**  
   ```bash
   ./delete_log.sh
   ```

4. **Capture Data**  
   ```bash
   ./serial.sh
   ```
   Enter your message, then Ctrl‑C to stop.

5. **Plot Results**  
   ```bash
   ./plot.sh
   ```

6. **Plot Circuit Schematic**  
   ```bash
   poetry run python schematic.py
   ```

## File Structure

- `datalink.ino` — Arduino sketch (LED → LDR data‑link).
- `serial_reader.py` — Sends message, reads sensor values to `arduino_log.txt`.
 - `log.py` — Loads and plots `arduino_log.txt`.
 - `schematic.py` — Plots the circuit schematic diagram (uses Plotly).
- `find_port.sh`, `serial.sh`, `plot.sh`, `delete_log.sh` — Helper scripts.
- `saved_logs/` — Archive directory for previous logs.
- `pyproject.toml`, `poetry.lock` — Python project config.

## Saving Logs

Move or copy `arduino_log.txt` into `saved_logs/` to keep past captures.