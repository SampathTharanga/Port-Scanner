import socket
from banner import print_banner 

def port_scan(target, ports):
    open_ports = []
    closed_ports = []
    print("Scanning target: {target}")
    for port in ports:
        try:
            # CREATE A SOCKET OBJECT
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # SET TIMEOUT TO 1 SECOND
            sock.settimeout(1)

            # CONNECT TO THE PORT
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            else:
                print(f"Port {port}: Closed")
                closed_ports.append(port)
            
            # CLOSE THE SOCKET
            sock.close()

        except KeyboardInterrupt:
            print("\nScan terminated by user.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Couldn't connect to server.")
            break
    return open_ports, closed_ports


if __name__ == "__main__":
    target_host = input("Enter the target hostname or IP address: ")
    port_range = input("Enter the range of ports to scan (e.g., 1-100): ")

    # PARSE THE PORT RANGE
    start_port, end_port = map(int, port_range.split('-'))
    port_list = range(start_port, end_port + 1)

    open_ports, closed_ports = port_scan(target_host, port_list)

    if open_ports:
        print("\nOpen ports:")
        print(', '.join(map(str, open_ports)))
    else:
        print("\nNo open ports found.")

    
    if closed_ports:
        print("\nClosed ports:")
        print(', '.join(map(str, closed_ports)))
    else:
        print("\nAll ports in the specified range are open.")