from control.matlab import *
from control import impulse_response,step_response
import numpy as np
import matplotlib.pyplot as  plt
#np.set_printoptions(precision=3,suppress=True,threshold='nan')


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


def test_controllability(b_mat, a_mat):
    """
    Functions determines if a systems defined by the B
    is contollable
    """
    #Controllability test
    con = np.array(b_mat)
    for i in range(1, 7):
        a = np.linalg.matrix_power(a_mat, i)
        mul = np.matmul(a, b_mat)
        #con = np.concatenate((con,mul),axis=1)
        con = np.concatenate((con, mul), axis=1)

    det = np.linalg.det(con)
    print("Determinate:\t{}".format(det))  #IF ZERO SYSTEM CONTROLLABLE
    


def get_control_gains(A, B, Q, R):
    """
    Function returns the state feedback gains,
    solution to he ricarti equations
    Eignevalues of the closed loop system
    """


    return lqr(A,B,Q,R)

def sys_res(state_gains,A,B,C,D):
    """
    Function plots the system step response given state gains

    """
    # THESE VALUES CONTROL THE SYSTEM BUT TAKES TO LONG FOR THE PENDULUM TO STABALIZE
    #K = np.array([31.623, 795.708, -30141.523, -4524.976,
    #          0, 31.854, 35.542]).reshape(1, 7)

    BK = np.matmul(B, state_gains)
    BKC = np.matmul(BK, C)
    #MOVE EIGS OF A using K
    e, v = np.linalg.eig(A)
    es, v = np.linalg.eig(A-BKC)


    A = A-BKC
    T = np.arange(0, 120, 1)
    sys = ss(A, B, C, D)
    t, yout = step_response(sys, T)
    plot_states(t, yout)




#K = np.array([31.623, 795.708, -30141.523, -4524.976,0, 31.854, 35.542]).reshape(1, 7)
#sys_res(K, A, B, C, D)


Q = np.identity(7)
R = .001
K,S,E = get_control_gains(A,B,Q,R)

print(k)
exit() 
