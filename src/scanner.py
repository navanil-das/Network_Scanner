import socket
from concurrent.futures import ThreadPoolExecutor
from src.banner_grabber import grab_banner

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            banner = grab_banner(target, port)
            return (port, banner)

    except:
        pass

    return None


def scan_ports(target, ports):
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)

    for result in results:
        if result:
            open_ports.append(result)

    return open_ports
