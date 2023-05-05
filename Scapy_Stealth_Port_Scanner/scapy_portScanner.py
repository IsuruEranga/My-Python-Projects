from scapy.all import *
from tqdm import tqdm
import argparse
import logging


def stealth_ports_scan(target_ip, start_port, end_port):
    
    logging.getLogger("scapy").setLevel(logging.ERROR)

    open_ports = []
    closed_ports = []
    
    for port in tqdm(range(start_port, end_port), desc="Scanning"):
        src_port = RandShort()
        response = sr1(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="S"), timeout=2, verbose=0)
        if response is not None:
            if response[TCP].flags == "SA":  # SYN-ACK
                send(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)  # RST
                open_ports.append(port)
            elif response[TCP].flags == "RA":  # RST-ACK
                closed_ports.append(port)
        else:
            closed_ports.append(port)

    # return open_ports, closed_ports
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="A simple TCP stealth port scanner using Scapy")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("--start_port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end_port", type=int, default=1024, help="End port (default: 1024)")

    args = parser.parse_args()
    
    print(f"scanning {args.target_ip}, from port {args.start_port}, to port {args.end_port}")

    #open_ports, closed_ports = stealth_ports_scan(args.target_ip, args.start_port, args.end_port)
    open_ports = stealth_ports_scan(args.target_ip, args.start_port, args.end_port)

    #print(f"Open ports: {open_ports}")
    #print(f"Closed ports: {closed_ports}")

    if open_ports:
        print(f"Open ports on {args.target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {args.target_ip}.")


if __name__ == "__main__":
    main()
