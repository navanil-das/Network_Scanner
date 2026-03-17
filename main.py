import argparse
from src.scanner import scan_ports
from src.utils import parse_ports

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("--target", required=True)
    parser.add_argument("--ports", default="1-1024")

    args = parser.parse_args()

    target = args.target
    ports = parse_ports(args.ports)

    print(f"\nScanning {target}...\n")

    results = scan_ports(target, ports)

    for port, banner in results:
        if banner:
            print(f"[OPEN] {port} -> {banner}")
        else:
            print(f"[OPEN] {port} -> Unknown Service")


if __name__ == "__main__":
    main()
save_to_json(target, results)
print("\nResults saved to results/scan_results.json")
