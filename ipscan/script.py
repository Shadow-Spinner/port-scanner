#! /usr/bin/python3
import socket
import sys
import nmap
banner=open("banner.txt","r")
print(banner.read())
print("<<<<....................................................................................>>>>")
host=(input("enter the IP address => "))
choice=int(input("enter 1 for finding ip \n      2 for ayc scan \n      3 for udp scan\n=> "))
if choice==1:
    try:
        def ip():
            print("IP address is => ",socket.gethostbyname(host))
        ip()
    except:
        print("can't connect to the target!!!")
elif choice==2:
    try:
        def tcpscan():
            result=nmap.PortScanner()
            print("checking....")
            result.scan(host,'22-443')
            ports=result[host]['tcp'].keys()
            proto=result[host].all_protocols()
            print("network protocol => ",proto)
            print("open ports => ",ports)
        tcpscan()
    except:
        print("can't connect to the target!!!")
elif choice==3:
    try:
        def udpscan():
            result=nmap.PortScanner()
            print("checking....")
            result.scan(host,'22-443')
            ports=result[host]['udp'].keys()
            proto=result[host].all_protocols()
            print("network protocol => ",proto)
            print("open ports => ",ports)
        udpscan()
    except:
        print("can't connect to the target!!!")
else:
    print("inappropriate value")
    sys.exit()