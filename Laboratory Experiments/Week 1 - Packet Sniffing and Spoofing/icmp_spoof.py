#! /usr/bin/python
from scapy.all import *
print ("SENDING SPOOFED ICMP PACKET...");
IPLayer = IP()
IPLayer.src="10.0.2.13"
IPLayer.dst="192.168.29.153"
ICMPpkt = ICMP()
pkt = IPLayer/ICMPpkt
pkt.show ()
send(pkt,verbose=0)