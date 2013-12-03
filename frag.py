#!/usr/bin/env python

from scapy.all import *

# targets = ["ubuntu2", "freebsd"]
targets = ["freebsd"]

pay1 = "Linux!! Nothing to see here ...\n"
pay2 = "Falun Gong! Now the Revolution!\n"
pay3 = "\x00" * 32

def main():
    for dip in targets:
        ip = IP( dst = dip, proto = 17, id = 12345, flags = 'MF' )
        udp = UDP( chksum = 0, sport = 8889, dport = 8888, len = 64 )
        pkt = ip / udp
        send(pkt)

        ip = IP( dst = dip, proto = 17, id = 12345, frag = 1, flags = 'MF' )
        pkt = ip / pay2
        send(pkt)

        ip = IP( dst = dip, proto = 17, id = 12345, frag = 1, flags = 'MF' )
        pkt = ip / pay1
        send(pkt)

        ip = IP( dst = dip, proto = 17, id = 12345, frag = 4, flags = 0 )
        pkt = ip / pay3
        send(pkt)

main()
