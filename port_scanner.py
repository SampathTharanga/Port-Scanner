import socket

def port_scan(target, ports):
    open_ports = []
    print("Scanning target: {target}")
    for port in ports:
        try:
            # CREATE A SOCKET OBJECT
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # SET TIMEOUT TO 1 SECOND
            sock.settimeout(1)
