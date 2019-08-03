import socket
import subprocess
import sys
from datetime import datetime

subprocess.call("", shell=True)
rmip = input("ENTER REMOTE HOST IP: ")
ps1 = int(input("ENTER START PORT NUMBER TO SCAN: "))
ps2 = int(input("ENTER LAST PORT NUMBER TO SCAN: "))
print("*"*40)
print("SCANNING REMOTE IP's...")
print("*"*40)

t1 = datetime.now()
try:
    for port in range(ps1, ps2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((rmip, port))
        if result == 0:
            print("PORT OPEN --> ", port)
            # print desc[port]
        sock.close()

except KeyboardInterrupt:
    print("SCANNING INTERRUPTED!")
    sys.exit()

except Exception as e:
    print(e)
    sys.exit()

t2 = datetime.now()

timeTotal = t2 - t1
print("SCANNING COMPLETE IN", timeTotal)

