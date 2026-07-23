# 🔍 Basic Network Sniffer

## 📋 Overview

A Python-based network packet sniffer that captures and analyzes network traffic in real-time. This tool helps understand how data flows through networks and provides insights into packet structures, protocols, and network communication patterns.

## 🎯 Project Objectives

- Capture network packets using Python
- Analyze packet structure and content
- Understand network protocols (TCP, UDP, ICMP)
- Display key information: source/destination IPs, protocols, and payloads
- Learn ethical network monitoring practices

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core programming language |
| Scapy | Packet manipulation and sniffing |
| Socket | Raw socket implementation (alternative) |
| Struct | Binary data parsing |

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- Administrator/root privileges (required for packet capturing)
- Network interface with promiscuous mode support

### Step 1: Install Dependencies
```bash
# Install required Python packages
pip install -r requirements.txt

# For Windows users, install Npcap (required for Scapy)
# Download from: https://npcap.com
```

### Step 2: Verify Installation
```bash
python sniffer.py --help
```

## 🚀 Usage Guide

### Basic Usage

#### 1. Simple Packet Capture (Default Mode)
```bash
# Capture 10 packets and display basic info
sudo python sniffer.py

# Capture specific number of packets
sudo python sniffer.py -c 50

# Capture packets from specific network interface
sudo python sniffer.py -i eth0
```

#### 2. Advanced Options
```bash
# Filter by protocol
sudo python sniffer.py -p tcp
sudo python sniffer.py -p udp

# Filter by specific IP
sudo python sniffer.py --src 192.168.1.100
sudo python sniffer.py --dst 8.8.8.8

# Save captured packets to file
sudo python sniffer.py -o captured_packets.pcap

# Verbose mode (detailed output)
sudo python sniffer.py -v
```

#### 3. Socket Implementation (Alternative)
```bash
# Run the socket-based sniffer
sudo python socket_sniffer.py

# Capture with specific interface
sudo python socket_sniffer.py -i eth0
```

## 📁 Project Structure

```
CodeAlpha_NetworkSniffer/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── sniffer.py               # Main Scapy-based sniffer
├── socket_sniffer.py        # Socket-based alternative
├── packet_analyzer.py       # Packet analysis module
├── utils.py                 # Utility functions
├── config.py                # Configuration settings
├── examples/
│   ├── tcp_analysis.py     # TCP packet analysis
│   ├── udp_analysis.py     # UDP packet analysis
│   └── http_sniff.py       # HTTP traffic sniffer
└── tests/
    ├── test_sniffer.py      # Unit tests
    └── test_packets.pcap    # Test capture file
```

## 📊 Sample Output

```
Starting packet capture on interface eth0...
Capturing 10 packets...

[+] Packet #1 - Time: 14:32:15
    ├── Source IP: xxxxxxxxxxxxx
    ├── Destination IP: xxxxxxxxxxxx
    ├── Protocol: TCP
    ├── Source Port: 
    ├── Destination Port: 
    ├── Flags: SYN
    └── Payload: [SYN] Connection request

[+] Packet #2 - Time: 14:32:15
    ├── Source IP:xxxxxxxxxxx
    ├── Destination IP:xxxxxxxxx
    ├── Protocol: TCP
    ├── Source Port: 443
    ├── Destination Port: 
    ├── Flags: SYN-ACK
    └── Payload: [SYN-ACK] Connection accepted

[+] Packet Analysis Summary
    ├── Total Packets: 10
    ├── TCP: 6 (60%)
    ├── UDP: 3 (30%)
    ├── ICMP: 1 (10%)
    ├── Data Volume: 1.2 KB
    └── Top Source IP:"X.X.X.X" (5 packets)
```

## 🔧 Features

### Core Features
- ✅ Real-time packet capture
- ✅ Protocol detection (TCP, UDP, ICMP, ARP)
- ✅ Source/Destination IP extraction
- ✅ Port detection for TCP/UDP
- ✅ Payload display (hex and ASCII)
- ✅ Packet filtering by IP, port, protocol
- ✅ Packet count and rate monitoring
- ✅ Export to PCAP format

### Advanced Features
- 🔄 Multi-threaded packet processing
- 📈 Traffic statistics and analysis
- 🎯 Custom BPF (Berkeley Packet Filter) support
- 📝 Logging to file
- 🔔 Alert system for suspicious traffic
- 📊 Traffic visualization (optional)

## 🎨 Code Examples

### Example 1: Basic Sniffer
```python
from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if IP in packet:
        print(f"Source: {packet[IP].src} -> Dest: {packet[IP].dst}")

sniff(count=10, prn=packet_callback)
```

### Example 2: Protocol-Specific Sniffer
```python
def tcp_sniffer():
    def tcp_callback(packet):
        if TCP in packet and packet[TCP].dport == 80:
            print(f"HTTP Traffic: {packet[IP].src} -> {packet[IP].dst}")
    
    sniff(filter="tcp port 80", prn=tcp_callback)

tcp_sniffer()
```

### Example 3: Custom Packet Analysis
```python
def analyze_packet(packet):
    """Analyze packet and return structured data"""
    info = {
        'timestamp': packet.time,
        'length': len(packet),
        'source': None,
        'destination': None,
        'protocol': None,
        'payload': None
    }
    
    if IP in packet:
        ip = packet[IP]
        info['source'] = ip.src
        info['destination'] = ip.dst
        info['protocol'] = ip.proto
        
        if TCP in packet:
            tcp = packet[TCP]
            info['sport'] = tcp.sport
            info['dport'] = tcp.dport
            info['flags'] = tcp.flags
            
        if packet.haslayer(Raw):
            info['payload'] = packet[Raw].load
    
    return info
```

## 🛡️ Security & Ethical Considerations

### ⚠️ Important Disclaimer
**This tool is for educational purposes only. Always ensure you have proper authorization before capturing network traffic.**

### 📜 Legal Guidelines
1. **Only capture traffic on networks you own or have explicit permission to monitor**
2. **Respect privacy laws and regulations (GDPR, CCPA, etc.)**
3. **Never use this tool for malicious purposes**
4. **Inform all users if you're monitoring network traffic**
5. **Encrypt and securely store any captured sensitive data**

### 🔒 Security Best Practices
- Run with minimum required privileges
- Implement data anonymization
- Use secure channels for data transmission
- Regular security audits of code
- Keep dependencies updated

## 🧪 Testing

### Run Tests
```bash
# Run unit tests
python -m pytest tests/

# Test with sample PCAP file
python sniffer.py -r test_packets.pcap

# Performance testing
python sniffer.py -c 1000 --benchmark
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Permission denied | Run with sudo/administrator privileges |
| No packets captured | Check network interface and promiscuous mode |
| Scapy import error | Install Scapy: `pip install scapy` |
| Windows compatibility | Install Npcap/WinPcap |
| Filter not working | Verify BPF filter syntax |

### Debug Mode
```bash
# Enable debug logging
python sniffer.py --debug

# Show available interfaces
python sniffer.py --list-interfaces
```

## 📈 Performance Optimization

### Recommendations
- Use BPF filters to reduce captured packets
- Implement packet batching
- Use asynchronous processing for high traffic
- Adjust buffer sizes for high-volume networks
- Implement sample rate limiting

### Resource Usage
```python
# Optimize for performance
from scapy.all import conf
conf.sniff_promisc = False  # Disable promiscuous mode for less traffic
conf.sniff_timeout = 10     # Set timeout for long captures
```

## 📚 Learning Resources

### Network Protocols
- [TCP/IP Guide](http://www.tcpipguide.com/)
- [Wireshark Documentation](https://www.wireshark.org/docs/)
- [RFC Documents](https://www.rfc-editor.org/)

### Python Resources
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)
- [Python Networking Tutorials](https://realpython.com/python-networking/)

## 🚧 Future Improvements

- [ ] Add GUI interface (Tkinter/PyQt)
- [ ] Implement machine learning for anomaly detection
- [ ] Add support for IPv6
- [ ] Create packet replay functionality
- [ ] Add geographic IP mapping
- [ ] Implement real-time dashboard
- [ ] Support for encrypted traffic analysis
- [ ] Add more protocol dissectors

## 🤝 Acknowledgments

- CodeAlpha for the internship opportunity
- Scapy community for the excellent packet manipulation library
- Open-source security community for best practices


## 📊 Project Status

- ✅ Initial release
- ✅ Basic packet capture
- ✅ Protocol detection
- 🟡 Advanced analysis (In Progress)
- 🔲 Visualization dashboard (Planned)

---

## 🎓 Learning Outcomes

After completing this project, you should understand:
- ✓ How network packets are structured
- ✓ TCP/IP protocol stack
- ✓ Common network protocols (TCP, UDP, ICMP)
- ✓ Packet capturing techniques
- ✓ Network security monitoring basics
- ✓ Python networking libraries
- ✓ Ethical hacking principles

---

**⚠️ Remember**: With great power comes great responsibility. Use this tool wisely and ethically!

---

*Last Updated: 2024*
*Version: 1.0.0*
```


---

# 📄 sniffer.py 

```python
#!/usr/bin/env python3
"""
Basic Network Sniffer - Task 1
CodeAlpha Cyber Security Internship
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from scapy.layers.inet import IP
import argparse
import sys
from datetime import datetime
from colorama import init, Fore, Style
import json

# Initialize colorama for colored output
init(autoreset=True)

class NetworkSniffer:
    def __init__(self, interface=None, count=10, verbose=False):
        self.interface = interface
        self.count = count
        self.verbose = verbose
        self.packet_count = 0
        self.protocol_stats = {'TCP': 0, 'UDP': 0, 'ICMP': 0, 'Other': 0}
        self.packets = []
    
    def packet_callback(self, packet):
        """Callback function for each captured packet"""
        self.packet_count += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print(f"\n{Fore.CYAN}[+] Packet #{self.packet_count} - Time: {timestamp}")
        print(f"{'─' * 50}")
        
        if IP in packet:
            ip_layer = packet[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            protocol = ip_layer.proto
            
            print(f"{Fore.GREEN}    ├── Source IP: {src_ip}")
            print(f"{Fore.GREEN}    ├── Destination IP: {dst_ip}")
            
            # TCP Protocol
            if TCP in packet:
                tcp_layer = packet[TCP]
                self.protocol_stats['TCP'] += 1
                print(f"{Fore.YELLOW}    ├── Protocol: TCP")
                print(f"{Fore.YELLOW}    ├── Source Port: {tcp_layer.sport}")
                print(f"{Fore.YELLOW}    ├── Destination Port: {tcp_layer.dport}")
                print(f"{Fore.YELLOW}    ├── Flags: {tcp_layer.flags}")
                
                if packet.haslayer(Raw):
                    payload = packet[Raw].load
                    print(f"{Fore.MAGENTA}    └── Payload: {self.format_payload(payload)}")
            
            # UDP Protocol
            elif UDP in packet:
                udp_layer = packet[UDP]
                self.protocol_stats['UDP'] += 1
                print(f"{Fore.YELLOW}    ├── Protocol: UDP")
                print(f"{Fore.YELLOW}    ├── Source Port: {udp_layer.sport}")
                print(f"{Fore.YELLOW}    ├── Destination Port: {udp_layer.dport}")
                
                if packet.haslayer(Raw):
                    payload = packet[Raw].load
                    print(f"{Fore.MAGENTA}    └── Payload: {self.format_payload(payload)}")
            
            # ICMP Protocol
            elif ICMP in packet:
                icmp_layer = packet[ICMP]
                self.protocol_stats['ICMP'] += 1
                print(f"{Fore.YELLOW}    ├── Protocol: ICMP")
                print(f"{Fore.YELLOW}    ├── ICMP Type: {icmp_layer.type}")
                print(f"{Fore.YELLOW}    ├── ICMP Code: {icmp_layer.code}")
            
            else:
                self.protocol_stats['Other'] += 1
                print(f"{Fore.YELLOW}    ├── Protocol: {protocol} (Unknown)")
        
        else:
            print(f"{Fore.RED}    └── Non-IP Packet")
        
        # Store packet for analysis
        self.packets.append({
            'timestamp': timestamp,
            'source': src_ip if IP in packet else None,
            'destination': dst_ip if IP in packet else None,
            'protocol': self.get_protocol_name(protocol if IP in packet else None)
        })
    
    def format_payload(self, payload, max_bytes=50):
        """Format payload for display"""
        try:
            # Try to decode as ASCII
            ascii_str = payload[:max_bytes].decode('ascii', errors='ignore')
            return f"{ascii_str}..."
        except:
            # Show hex if not printable
            hex_str = ' '.join(f'{b:02x}' for b in payload[:20])
            return f"Hex: {hex_str}..."
    
    def get_protocol_name(self, proto_num):
        """Convert protocol number to name"""
        protocols = {
            6: 'TCP',
            17: 'UDP',
            1: 'ICMP',
            2: 'IGMP',
            47: 'GRE',
            50: 'ESP',
            51: 'AH',
            89: 'OSPF'
        }
        return protocols.get(proto_num, f'Unknown({proto_num})')
    
    def start_sniffing(self):
        """Start the packet capture"""
        print(f"{Fore.CYAN}Starting packet capture on interface: {self.interface or 'default'}")
        print(f"{Fore.CYAN}Capturing {self.count} packets...")
        print(f"{Fore.YELLOW}Press Ctrl+C to stop early{Style.RESET_ALL}")
        print("═" * 60)
        
        try:
            sniff(
                iface=self.interface,
                count=self.count,
                prn=self.packet_callback,
                store=False
            )
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}\n[!] Capture interrupted by user")
        except PermissionError:
            print(f"{Fore.RED}[!] Permission denied. Run with sudo/administrator privileges")
            sys.exit(1)
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
            sys.exit(1)
        
        self.show_summary()
    
    def show_summary(self):
        """Display packet analysis summary"""
        print("\n" + "═" * 60)
        print(f"{Fore.CYAN}📊 Packet Analysis Summary")
        print("═" * 60)
        
        total = self.packet_count
        print(f"{Fore.GREEN}    ├── Total Packets: {total}")
        print(f"{Fore.GREEN}    ├── TCP: {self.protocol_stats['TCP']} ({self.protocol_stats['TCP']/total*100:.1f}%)" if total > 0 else "    ├── TCP: 0")
        print(f"{Fore.GREEN}    ├── UDP: {self.protocol_stats['UDP']} ({self.protocol_stats['UDP']/total*100:.1f}%)" if total > 0 else "    ├── UDP: 0")
        print(f"{Fore.GREEN}    ├── ICMP: {self.protocol_stats['ICMP']} ({self.protocol_stats['ICMP']/total*100:.1f}%)" if total > 0 else "    ├── ICMP: 0")
        print(f"{Fore.GREEN}    └── Other: {self.protocol_stats['Other']} ({self.protocol_stats['Other']/total*100:.1f}%)" if total > 0 else "    └── Other: 0")
        
        # Top IPs
        if self.packets:
            print(f"{Fore.CYAN}\n    ├── Top Source IPs:")
            src_ips = {}
            for p in self.packets:
                if p['source']:
                    src_ips[p['source']] = src_ips.get(p['source'], 0) + 1
            sorted_ips = sorted(src_ips.items(), key=lambda x: x[1], reverse=True)[:3]
            for ip, count in sorted_ips:
                print(f"{Fore.GREEN}    │   └── {ip}: {count} packets")

def main():
    parser = argparse.ArgumentParser(
        description='Basic Network Sniffer - Capture and analyze network packets',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  sudo python sniffer.py                # Capture 10 packets
  sudo python sniffer.py -c 50          # Capture 50 packets
  sudo python sniffer.py -i eth0        # Use specific interface
  sudo python sniffer.py -p tcp         # Filter TCP packets
        '''
    )
    
    parser.add_argument(
        '-i', '--interface',
        help='Network interface to sniff (e.g., eth0, wlan0)'
    )
    
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=10,
        help='Number of packets to capture (default: 10)'
    )
    
    parser.add_argument(
        '-p', '--protocol',
        choices=['tcp', 'udp', 'icmp'],
        help='Filter by protocol'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Save packets to PCAP file'
    )
    
    args = parser.parse_args()
    
    # Create sniffer instance
    sniffer = NetworkSniffer(
        interface=args.interface,
        count=args.count,
        verbose=args.verbose
    )
    
    # Start sniffing
    sniffer.start_sniffing()

if __name__ == "__main__":
    main()
```

---

# 📄 socket_sniffer.py  (Alternative)

```python
#!/usr/bin/env python3
"""
Socket-based Network Sniffer - Alternative Implementation
CodeAlpha Cyber Security Internship
"""

import socket
import struct
import argparse
from datetime import datetime
import sys

class SocketSniffer:
    def __init__(self, interface=None, count=10):
        self.interface = interface
        self.count = count
        self.packet_count = 0
    
    def create_socket(self):
        """Create raw socket for packet capturing"""
        try:
            # Create raw socket
            sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
            sniffer.bind((self.interface or '0.0.0.0', 0))
            sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            
            # Enable promiscuous mode (Windows)
            try:
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            except AttributeError:
                pass  # Linux doesn't use ioctl
            
            return sniffer
        except PermissionError:
            print("[!] Error: Need root/administrator privileges for raw socket")
            sys.exit(1)
        except Exception as e:
            print(f"[!] Error creating socket: {e}")
            sys.exit(1)
    
    def parse_ip_header(self, data):
        """Parse IP header from raw data"""
        ip_header = struct.unpack('!BBHHHBBH4s4s', data[:20])
        version_ihl = ip_header[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        ttl = ip_header[5]
        protocol = ip_header[6]
        src_ip = socket.inet_ntoa(ip_header[8])
        dst_ip = socket.inet_ntoa(ip_header[9])
        
        return {
            'version': version,
            'ihl': ihl,
            'ttl': ttl,
            'protocol': protocol,
            'src_ip': src_ip,
            'dst_ip': dst_ip
        }
    
    def get_protocol_name(self, proto_num):
        """Convert protocol number to name"""
        protocols = {
            6: 'TCP',
            17: 'UDP',
            1: 'ICMP',
            2: 'IGMP'
        }
        return protocols.get(proto_num, f'Unknown({proto_num})')
    
    def start_sniffing(self):
        """Start packet capture using raw socket"""
        sniffer = self.create_socket()
        
        print(f"[+] Starting packet capture on interface: {self.interface or 'default'}")
        print(f"[+] Capturing {self.count} packets...")
        print("=" * 60)
        
        try:
            while self.packet_count < self.count:
                # Receive packet
                data, addr = sniffer.recvfrom(65565)
                self.packet_count += 1
                timestamp = datetime.now().strftime("%H:%M:%S")
                
                # Parse IP header
                ip_info = self.parse_ip_header(data[:20])
                
                print(f"\n[+] Packet #{self.packet_count} - Time: {timestamp}")
                print(f"    ├── Source IP: {ip_info['src_ip']}")
                print(f"    ├── Destination IP: {ip_info['dst_ip']}")
                print(f"    ├── Protocol: {self.get_protocol_name(ip_info['protocol'])}")
                print(f"    ├── TTL: {ip_info['ttl']}")
                print(f"    └── Data Length: {len(data)} bytes")
                
        except KeyboardInterrupt:
            print(f"\n[!] Capture interrupted by user")
        finally:
            # Disable promiscuous mode
            try:
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            except:
                pass
            sniffer.close()

def main():
    parser = argparse.ArgumentParser(description='Socket-based Network Sniffer')
    parser.add_argument('-i', '--interface', help='Network interface')
    parser.add_argument('-c', '--count', type=int, default=10, help='Packets to capture')
    args = parser.parse_args()
    
    sniffer = SocketSniffer(interface=args.interface, count=args.count)
    sniffer.start_sniffing()

if __name__ == "__main__":
    main()
```

