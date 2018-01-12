import machine
"""
Pin Labels

#Pin Definitions
D0 = 16;
D1 = 5;
D2 = 4;
D3 = 0;
D4 = 2;
D5 = 14;
D6 = 12;
D7 = 13;
D8 = 15;
D9 = 3;
D10 = 1;


PD5 = Pin(14,Pin.OUT) Right Wheel
PD6 = Pin(12,Pin.OUT) Right Wheel
PD7 = Pin(13,Pin.OUT) Left Wheel
PD9 = Pin(3,Pin.OUT)  Left Wheel
PD10 = Pin(1,Pin.OUT) Enable Pin


pwmD5
pwmD6
pwmD7
pwmD9
"""

"""
""Enables Pins on Motor Driver
""Val: 1 means Enables 0 means disables
"""
def EnOrDis(val):
    global PD10
    if val is 1: 
        PD10.value(1)
    else:
        PD10.value(0)

"""
"" Moves Robot forward or backward
"" if dcycle<0 move backwards dycle>0 move forward
"""
def moveRobot(dcycle):
    global pwmD5    #Forwad Pin right
    global pwmD6    #Backward Pin Right
    global pwmD7    #Forward Pin Left
    global pwmD9    #Backward Pin Right
    

    if dcycle < 0:
        dcycle = abs(dcycle)
        pwmD5.duty(0)
        pwmD7.duty(0)
        pwmD6.duty(dcycle)
        pwmD9.duty(dcycle)
    else:
        pwmD5.duty(dcycle)
        pwmD7.duty(dcycle)
        pwmD6.duty(0)
        pwmD9.duty(0)

"""
"" Deactivate pwm Pins
"""
def DeactivatePins():
    global pwmD5, pwmD6, pwmD7, pwmD9, PD10

    pwmD5.deinit()
    pwmD6.deinit()
    pwmD7.deinit()
    pwmD9.deinit()
    PD10.off()



"""
#Defining pins for pwm
PD5 = machine.Pin(14) #RIGHT WHEEL PWM
PD6 = machine.Pin(12) #RIGHT WHEEL PWM
PD7 = machine.Pin(13) #LEFT WHEEL PWM
PD9 = machine.Pin(3)  #LEFT WHEEL PWM
PD10 = machine.Pin(1,machine.Pin.OUT) #ENABLE PIN

pwmD5 = machine.PWM(PD5)
pwmD6 = machine.PWM(PD6)
pwmD7 = machine.PWM(PD7)
pwmD9 = machine.PWM(PD9)

pwmD5.freq(500) #Forward Pin Right
pwmD6.freq(500) #Backward Pin Right
pwmD7.freq(500) #Forward Pin Left
pwmD9.freq(500) #Backward Pin Left
"""

import page.py
