def parse_ports(port_range):
    start, end = port_range.split("-")
    return range(int(start), int(end) + 1)
import subprocess
import platform

def detect_os(target):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", target]

    try:
        output = subprocess.check_output(command).decode()

        if "ttl=64" in output.lower():
            return "Linux/Unix"
        elif "ttl=128" in output.lower():
            return "Windows"
        else:
            return "Unknown"
    except:
        return "Unknown"
