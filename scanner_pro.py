import scapy.all as scapy
import socket

# 1. Network Scan (Devices dhoondhna)
def scan_network(ip_range):
    print(f"[*] Scanning Network: {ip_range}")
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered = scapy.srp(packet, timeout=2, verbose=False)[0]
    
    devices = []
    for sent, received in answered:
        devices.append(received.psrc)
    return devices

# 2. Port Scan (Khidkiyan check karna)
def scan_ports(target_ip):
    print(f"\n[*] Scanning Ports for: {target_ip}")
    open_ports = []
    # Common ports scan kar rahe hain
    for port in [21, 22, 23, 80, 443, 445, 5555, 8080]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Main Execution
if __name__ == "__main__":
    network = "192.168.1.0/24" # Apne network ki range yahan likhein
    active_devices = scan_network(network)
    
    for ip in active_devices:
        print(f"\n[+] Found Device: {ip}")
        ports = scan_ports(ip)
        if ports:
            print(f"[!] Open Ports: {ports}")
        else:
            print("[-] No common ports open.")