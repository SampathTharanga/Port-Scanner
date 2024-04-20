# Port Scanner

Port Scanner is a simple Python tool for scanning ports on a target host.

## Features

- Scan a range of ports on a target host
- Display open ports
- Simple to use

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/port-scanner.git
2. Navigate to the project directory:

   ```bash
   cd port-scanner
  
   ```
3. Run the script:
   ```bash
   python port_scanner.py

   ```
## Usage
1. Enter the target hostname or IP address when prompted.
2. Enter the range of ports to scan (e.g., 1-100) when prompted.
3. The script will scan each port in the specified range and display whether it is open or closed.

## Example
```
Enter the target hostname or IP address: example.com
Enter the range of ports to scan (e.g., 1-100): 1-100

Scanning target: example.com
Port 22: Closed
Port 80: Open
Port 443: Open

Open ports:
80, 443
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
