import machine
import socket
import os
from html import html


files = os.listdir()

addr = socket.getaddrinfo('0.0.0.0',80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on',addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb',0)
    
    """while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break"""

    request = cl.recv(1024)
    print(str(request))
    #print(str(request.find('/?Dcycle')))

    rows = ['<tr><td>%s</td></tr>' % str(p) for p in files]
    response = html % '\n'.join(rows)
    #print(response)
    cl.send(response)
    cl.close()

s.close()
