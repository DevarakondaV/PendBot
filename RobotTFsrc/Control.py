from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

m_total = 298.0/1000 #mass cart
m_2 = 33.0/1000   #mass Pend
m_1 = m_total-m_2
g = 9.81
l = (30.5/2.0)/100.0    #Pendulum COG length
k = 0.145       #motor constant
R = 3.0/100     #Radius Wheel
m_wheel = 25.0/1000
I = m_wheel*(np.power(R,2))


#Testing
TFN = [0,.102]
TFD = [0.0446,0,-1]

WTFN = [0.391,0]
WTFD = [.5,1]

TF = tf(TFN,TFD)
WTF = tf(WTFN,WTFD)

print(TF)
print(WTF)

CN = [1,20,100]
CD = [1,0]

CTF = 8*tf(CN,CD)

SysTF = series(WTF,TF)
SysTF = series(CTF,SysTF)
SysTF  = feedback(SysTF,2.35)
print(SysTF)
#a,b = rlocus(SysTF)
#plt.show()
The,T = step(SysTF)
plt.plot(T,The)
plt.show()




"""
#Wheel Actuator TF
WTFN = [I/R,0]
WTFD = [0,1]

TFN = [0,1]
TFD = [(l*(m_1+m_2))-(l*m_2),0,-g*(m_1+m_2)]

WTF = tf(WTFN,WTFD)
TF = tf(TFN,TFD)

"""
