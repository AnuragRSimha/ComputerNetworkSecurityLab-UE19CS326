#! /usr/bin/python
from scapy.all import *
print ("SENDING SPOOFED ICMP PACKET...");
IPLayer = IP()
for i in range(0,3):
    IPLayer.src="1.2.3.4"
    IPLayer.dst="10.0.2.13"
    ICMPpkt = ICMP()
    pkt = IPLayer/ICMPpkt
    pkt.show ()
    send(pkt,verbose=0)