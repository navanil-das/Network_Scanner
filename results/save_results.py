import json

def save_to_json(target, results):
    data = {
        "target": target,
        "open_ports": [
            {"port": port, "banner": banner}
            for port, banner in results
        ]
    }

    with open("results/scan_results.json", "w") as f:
        json.dump(data, f, indent=4)
