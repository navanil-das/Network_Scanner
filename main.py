import argparse
from src.scanner import scan_ports
from src.utils import parse_ports

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("--target", required=True, help="Target IP address")
    parser.add_argument("--ports", default="1-1024", help="Port range (e.g. 1-1000)")

    args = parser.parse_args()

    target = args.target
    ports = parse_ports(args.ports)

    print(f"\nScanning {target}...\n")

    open_ports = scan_ports(target, ports)

    for port in open_ports:
        print(f"[OPEN] {port}")


if __name__ == "__main__":
    main()
