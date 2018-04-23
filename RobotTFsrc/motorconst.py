import numpy as np
import matplotlib.pyplot as plt

#file dir
fsrc1 = "/home/vishnu/Documents/EngProjs/PendBot/PendBot/Data/700.txt"
fsrc2 = "/home/vishnu/Documents/EngProjs/PendBot/PendBot/Data/900.txt"

def get_data(src):
    ms = []
    av = []
    f = open(src,"r")
    f.readline()
    for line in f:
        a,b,c = line.split('\t')
        ms.append(int(b))
        av.append(float(c))
    f.close()

    return ms,av

ms1,av1 = get_data(fsrc1)
ms2,av2 = get_data(fsrc2)
av1 = np.average(av1)
av2 = np.average(av2)
v1 = (700.0/1023)*12
v2 = (900.0/1023)*12
k = (v1-v2)/(av1-av2)
print(v1,av1)
print(v2,av2)
print(k)


"""
z = np.polyfit(ms,av,4)
f = np.poly1d(z)

print(ms[-1])
x_new = np.linspace(ms[0],ms[-1],50)
y_new = f(x_new)

plt.plot(ms,av,'o',x_new,y_new)
plt.xlim([ms[0]-1,ms[-1]+1])
plt.show()
"""
