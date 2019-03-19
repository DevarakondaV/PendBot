from control.matlab import *
from control import impulse_response,step_response
import numpy as np
import matplotlib.pyplot as  plt
np.set_printoptions(precision=3,suppress=True,threshold='nan')


def plot_states(t,yout):
    """
    Makes a plot of the system
    
    args:
        t:  Time vector
        yout:   Vector of states
    """
    
    
    fig = plt.figure("response")
    plt.subplot(421)
    plt.plot(t,yout[0])
    plt.title("Cart Position")

    plt.subplot(422)
    plt.plot(t,yout[1])
    plt.title("Cart velocity")
    
    plt.subplot(423)
    plt.plot(t,yout[2])
    plt.title("Pendulum Angle")
    
    plt.subplot(424)
    plt.plot(t,yout[3])
    plt.title("Pendulum Ang. Vel.")
    
    plt.subplot(425)
    plt.plot(t,yout[4])
    plt.title("Motor Angle")
    
    plt.subplot(426)
    plt.plot(t,yout[5])
    plt.title("Motor Ang. Vel.")
    
    plt.subplot(427)
    plt.plot(t,yout[6])
    plt.title("Current")
    
    plt.show()


    

m1 = .5
m2 = .2
Imw = .003
Rw = .5
n = 2
l = .3
g = 9.8

b = .6456482
J = .12919318
K = .58034283
L = .25841064
R = .13691942



# STATE SPACE MODEL

A = np.array(
    [[0,    1,  0,                  0,  0,  0,                                          0],
     [0,    0,  m2*g/(m1),          0,  0,  -(Imw*b)/(n*m1*Rw*J),   -(Imw*K)/(n*m1*Rw*J)],
     [0,    0,  0,                  1,  0,  0,                              0],
     [0,    0,  (m1+m2)*g/(m1*l),   0,  0,  -(Imw*b)/(n*m1*Rw*J*l), -(Imw*K)/(n*m1*Rw*J*l)],   
     [0,    0,  0,                  0,  0,  1,                              0],
     [0,    0,  0,                  0,  0,  -b/J,                           K/J],
     [0,    0,  0,                  0,  0,  -K/J,                           -R/L]])

B = np.array([0,0,0,0,0,0,1/L]).reshape(7,1)
B = np.array([0,0,0,0,0,0,1/L]).reshape(7,1)
C = np.array([[1,0,0,0,0,0,0],[0,0,1,0,0,0,0]]).reshape(7,2)
C = np.identity(7)
D = np.array([0,0,0,0,0,0,0]).reshape(7,1)


"""
#Controllability test
con = np.array(B)
for i in range(1,7):
    a = np.linalg.matrix_power(A,i)
    mul = np.matmul(a,B)
    #con = np.concatenate((con,mul),axis=1)
    con = np.concatenate((con,mul),axis=1)
det = np.linalg.det(con)
print("Determinate:\t{}".format(det))  #IF ZERO SYSTEM CONTROLLABLE
"""


# THESE VALUES CONTROL THE SYSTEM BUT TAKES TO LONG FOR THE PENDULUM TO STABALIZE
K = np.array([31.623,795.708,-30141.523,-4524.976,0,31.854,35.542]).reshape(1,7)
BK = np.matmul(B,K)
BKC = np.matmul(BK,C)
#MOVE EIGS OF A using K
e,v = np.linalg.eig(A)
es,v = np.linalg.eig(A-BKC)



A = A-BKC
T = np.arange(0,120,1)
sys = ss(A,B,C,D)
t,yout = step_response(sys,T)
plot_states(t,yout)


"""
print(e)
print(es)
X = [x.real for x in e]
Y = [x.imag for x in e]
plt.scatter(X,Y,color='r',marker='o')
X = [x.real for x in es]
Y = [x.imag for x in es]
plt.scatter(X,Y,color='b',marker='+')
plt.show()

print(np.shape(a),np.shape(bb))
print(np.shape(cc),np.shape(dd))
plt.show()

Out,T = step(sp)
plt.plot(T,Out)
plt.show()

a = np.array(
    [[0,    1,  0,              0],
     [0,    0,  (A*m2*l*g)/Ip,  0],
     [0,    0,  0,              1],
     [0,    0,  (m1+m2)*C*g,    0]])


a = np.array(
    [[0,    1,  0,              0],
     [0,    0,  (m2**2*g*l**2)/(Ip*(m1+m2)+(m1*m2*l**2)),  0],
     [0,    0,  0,              1],
     [0,    0,  ((m1+m2)*m2*g*l)/(Ip*(m1+m2)+(m1*m2*l**2)),    0]])


bb = np.array([0,0,0,0,0,0,1/L])
cc = np.array([[1,0,0,0,0,0,0],[0,0,1,0,0,0,0]])
time = np.arange(0,15,.1)
inputs = np.sin(time)
#inputs = np.array([0 for i in range(0,24)]+[25]+[0 for i in range(0,125)])

state_vals = []
#states_init = np.zeros((7))
#state_vals.append(states_init)
y = []
y.append(np.zeros(2))

tt = 0
for i,t in zip(inputs,time):
    states_init = np.array([0,0,i,0])
    #states_init = np.array([0,0,i,0,0,0,0])
    a = np.exp(a*(.1))
    states_init = np.matmul(a,states_init)
    state_vals.append(states_init)
    print(states_init)
    #y.append(np.matmul(cc,states_init))
cur = np.asarray(state_vals)[:,3]

plt.plot(time,inputs)
plt.plot(time,cur)
plt.show()

# STATE SPACE MODEL
A = (l)/((m1+m2)-(m2*l))
B = (Imw)/(n*Rw)
C = 1/((l*(m1+m2))-(m2*l))

aa = np.array(
    [[0,    1,  0,              0,  0,  0,              0],
     [0,    0,  (A*m2*l*g)/Ip,  0,  0,  -(A*B*b)/J,     (A*B*K)/J],
     [0,    0,  1,              0,  0,  0,              0],
     [0,    0,  (m1+m2)*C*g,    0,  0,  -(C*B*b)/J,     (C*B*K)/J],   
     [0,    0,  0,              0,  0,  1,              0],
     [0,    0,  0,              0,  0,  -b/J,           K/J],
     [0,    0,  0,              0,  0,  -K/J,           -R/L]])



XKd = 1000
XKp = 1
XKi = 0
XCN = [XKd,XKp,XKi]
XCD = [1,0]
Xcon = tf(XCN,XCD)

PKd = 1
PKp = -1
PKi = 1
PCN = [PKd,PKp,PKi]
PCD = [1,0]
Pcon = tf(PCN,PCD)

print(Xcon,Pcon)


TFX = tf([l,0,-g],[m1*l,0,-g*(m1+m2),0,0])
TFT = tf([1],[(m1+m2)*l-(m2*l),0,-(m1+m2)*g])
MD = tf([K],[J*L,J*R+b*L,R*b+K**2])
WD = tf([Imw,0],[n*Rw])



TFX = TFX*WD*MD
TFT = TFT*WD*MD

TFXF = feedback(TFX,Xcon)
TFTF = feedback(TFT,Pcon,sign=1)


#V = Xcon/(1+TFT*Pcon+TFX*Xcon)



#for i in inputs:
#    states_init = np.array([0 for p in range(0,2)]+[i]+[0 for p in range(0,4)])
#    states_init = np.matmul(a,states_init)
#    print(states_init)
#    state_vals.append(states_init)
#    #y.append(np.matmul(cc,states_init))

#cur = np.asarray(state_vals)[:,3]

#plt.plot(time,inputs)
#plt.plot(time,cur)
#plt.show()

"""
 
