from scapy.all import sniff, IP, TCP, UDP, ICMP
from scapy.layers.inet import IP

def packet_callback(packet):
    """Callback function to process each captured packet"""
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] Source IP: {ip_layer.src}")
        print(f"[+] Destination IP: {ip_layer.dst}")
        print(f"[+] Protocol: {ip_layer.proto}")
        
        # TCP Protocol
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"[+] Source Port: {tcp_layer.sport}")
            print(f+] Destination Port: {tcp_layer.dport}")
            if hasattr(tcp_layer, 'payload'):
                print(f"[+] Payload: {bytes(tcp_layer.payload)[:50]}...")
        
        # UDP Protocol
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"[+] Source Port: {udp_layer.sport}")
            print(f"[+] Destination Port: {udp_layer.dport}")
            if hasattr(udp_layer, 'payload'):
                print(f"[+] Payload: {bytes(udp_layer.payload)[:50]}...")
        
        # ICMP Protocol
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"[+] ICMP Type: {icmp_layer.type}")
            print(f"[+] ICMP Code: {icmp_layer.code}")

# Simple sniffing - captures 10 packets
print("Starting packet capture...")
sniff(count=10, prn=packet_callback)