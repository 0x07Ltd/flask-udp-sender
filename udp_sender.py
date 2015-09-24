from scapy.all import IP, UDP, L3RawSocket, conf
from scapy.all import send as scapy_send


def send(dest_ip, port, src_ip, payload, count=1):
    if dest_ip in ("127.0.0.1", "localhost"):
        conf.L3socket = L3RawSocket
    ip = IP(dst=dest_ip, src=src_ip)
    udp = UDP(dport=port)
    scapy_send(ip/udp/str(payload), count=count)
