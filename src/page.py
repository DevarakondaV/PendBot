import socket
import os
from html import html
from control import *
import utime

addr = socket.getaddrinfo('0.0.0.0',80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on',addr)

files = os.listdir();

def LedFlash():
    global Led
    Led.low()
    utime.sleep(2)
    Led.high()


def getIntVal(numb):
    rtnVal="";
    for i in numb:
        if i.isdigit():
            rtnVal = rtnVal+i

    return(int(rtnVal))


#Blink Connected
LedFlash()

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb',0)
    

    request = cl.recv(1024)
    request = str(request) 
    dcycle = request.find('/?Dcycle');  

    if (dcycle == 6):
        ind1 = dcycle+len('/?Dcycle=');
        ind2 = ind1+3;
        dcycle = request[ind1:ind2]
        if dcycle == "brk":
            DeactivatePins()
            break
        dcycle = getIntVal(dcycle)
        moveRobot(dcycle)

    rows = ['<tr><td>%s</td></tr>' % str(p) for p in files]
    response = html % '\n'.join(rows)
   
    cl.send(response)
    cl.close()

s.close()
