"""
Author: Guy D.
Last Modified: 31 JUL 19
Program: Scan an entire subnet with Python using ICMP ECHO request to view live hosts.
This sample code is provided for the purpose of illustration "AS IS" WITHOUT WARRANTY OF ANY KIND.
"""


import os
import platform
from datetime import datetime

net = input("ENTER NETWORK ADDRESS ")
net1 = net.split('.')
print(net1)
a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + a
print(net2)
st1 = int(input("Enter the stating Number --> "))
en1 = int(input("Enter the ending Number --> "))
en1 = en1 + 1
ops = platform.system()

if ops == "Windows":
    ping1 = 'ping -n 1'
elif ops == "Linux":
    ping1 = 'ping -c 1'
else:
    ping1 = 'ping -c 1'
t1 = datetime.now()
print("Scanning in Progress")

for ip in range(st1, en1):
    addr = net2 + str(ip)
    comm = ping1 + " " + addr
    echo = os.popen(comm)
    for line in echo.readlines():
        if 'ttl' in line.lower():
            print(addr, "--> IS LIVE")

t2 = datetime.now()
total = t2 - t1
print("Scanning Complete in", total)
