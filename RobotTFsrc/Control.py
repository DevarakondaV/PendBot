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



TFN = [0,1]
TFD = [(l*(m_1+m_2))-(l*m_2),0,-g*(m_1+m_2)]

#CN = [1,2,1]
CN = [1,-10,2]
CD = [1,3]

con = tf(CN,CD)
TF = tf(TFN,TFD)

sr = series(con,TF)

FBsys = feedback(TF,con)
The,T = step(FBsys)
#a,b = rlocus(sr)
#print(a,b)
#plt.plot(a[:,0],b)
#plt.show()
plt.plot(T,The)
plt.show()
