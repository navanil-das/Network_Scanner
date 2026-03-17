def parse_ports(port_range):
    start, end = port_range.split("-")
    return range(int(start), int(end) + 1)
  
