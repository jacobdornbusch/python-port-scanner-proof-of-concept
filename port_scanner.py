Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import socket
... import threading
... import concurrent.futures
... 
... # Function to scan a specific port on a target host
... def scan_port(host, port):
...     try:
...         # Create a TCP socket
...         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
...         sock.settimeout(1)  # Set socket timeout to 1 second
... 
...         # Connect to the target host and port
...         result = sock.connect_ex((host, port))
... 
...         # Check if the port is open or closed
...         if result == 0:
...             print(f"Port {port} on {host} is OPEN")
...         else:
...             print(f"Port {port} on {host} is CLOSED")
... 
...         # Close the socket
...         sock.close()
... 
...     except socket.error as e:
...         print(f"Error occurred while scanning port {port} on {host}: {str(e)}")
... 
... # Function to perform port scanning on a range of ports for a target host
... def port_scanner(host, start_port, end_port):
    print(f"Scanning ports on {host}...\n")

    # Create a thread pool for concurrent scanning of ports
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a list of futures for each port scan
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]

        # Wait for all port scans to complete
        concurrent.futures.wait(futures)

    print("\nPort scanning complete.")

# Entry point of the program
if __name__ == '__main__':
    # Set the target host and port range
    target_host = '69.16.238.59'
    start_port = 1
    end_port = 100

    # Perform port scanning
    port_scanner(target_host, start_port, end_port)
[DEBUG ON]
[DEBUG OFF]
import socket
import threading
import concurrent.futures

# Function to scan a specific port on a target host
def scan_port(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set socket timeout to 1 second

        # Connect to the target host and port
        result = sock.connect_ex((host, port))

        # Check if the port is open or closed
        if result == 0:
            print(f"Port {port} on {host} is OPEN")
        else:
            print(f"Port {port} on {host} is CLOSED")

        # Close the socket
        sock.close()

    except socket.error as e:
        print(f"Error occurred while scanning port {port} on {host}: {str(e)}")

# Function to perform port scanning on a range of ports for a target host
def port_scanner(host, start_port, end_port):
    print(f"Scanning ports on {host}...\n")

    # Create a thread pool for concurrent scanning of ports
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Create a list of futures for each port scan
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]

        # Wait for all port scans to complete
        concurrent.futures.wait(futures)

    print("\nPort scanning complete.")

# Entry point of the program
if __name__ == '__main__':
    # Set the target host and port range
    target_host = 'example.com'
    start_port = 1
    end_port = 100

    # Perform port scanning
