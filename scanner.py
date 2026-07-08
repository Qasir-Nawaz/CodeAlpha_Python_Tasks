import scapy.all as scapy
import socket

# Banner Grabbing function
def get_banner(target_ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target_ip, port))
        # Kuch services bina request ke banner nahi deti, isliye empty send karte hain
        sock.send(b'\r\n') 
        banner = sock.recv(1024)
        print(f"    [+] Banner on port {port}: {banner.decode().strip()}")
        sock.close()
    except:
        pass

# Network Scan
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

# Port Scan + Banner Grabbing
def scan_ports(target_ip):
    print(f"\n[*] Scanning Ports for: {target_ip}")
    # Common ports list
    for port in [21, 22, 23, 80, 443, 445, 5555, 8080]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"    [!] Port {port} is OPEN")
            get_banner(target_ip, port) # Banner try karega
        sock.close()

if __name__ == "__main__":
    network = "192.168.1.0/24"
    active_devices = scan_network(network)
    for ip in active_devices:
        scan_ports(ip)
