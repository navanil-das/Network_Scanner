from src.scanner import scan_ports

def main():
    target = input("Enter target IP: ")

    ports = range(1, 1025)

    print(f"\nScanning {target}...\n")

    open_ports = scan_ports(target, ports)

    for port in open_ports:
        print(f"[OPEN] {port}")


if __name__ == "__main__":
    main()
