import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return port
    except:
        pass

    return None


def scan_ports(target, ports):
    open_ports = []

    for port in ports:
        result = scan_port(target, port)
        if result:
            open_ports.append(result)

    return open_ports
