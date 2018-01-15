import machine
import utime
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
    global PD7
    if val is 1:
        PD7.high()
    else:
        PD7.low()

    """
    global PD10
    if val is 1: 
        #PD10.value(1)
        PD10.high()
    else:
        PD10.value(0)
        PD10.low()
    """

"""
"" Moves Robot forward or backward
"" if dcycle<0 move backwards dycle>0 move forward
"""
def moveRobot(dcycle):
    global pwmD5    #Forwad Pin right
    global pwmD6    #Backward Pin Right
    #global pwmD7    #Forward Pin Left
    #global pwmD8    #Backward Pin Right
    

    if dcycle < 0:
        dcycle = abs(dcycle)
        pwmD5.duty(0)
        #pwmD7.duty(0)
        pwmD6.duty(dcycle)
        #pwmD8.duty(dcycle)
    else:
        pwmD5.duty(dcycle)
        #pwmD7.duty(dcycle)
        pwmD6.duty(0)
        #pwmD8.duty(0)

    #Roll for 3 seconds
    utime.sleep(3)
    pwmD5.duty(0)
    pwmD6.duty(0)

"""
"" Deactivate pwm Pins
"""
def DeactivatePins():
    global pwmD5
    global pwmD6
    #global pwmD7
    #global pwmD9, PD10

    pwmD5.deinit()
    pwmD6.deinit()
    #pwmD7.deinit()
    #pwmD8.deinit()
    #PD10.off()




#Defining pins for pwm
PD5 = machine.Pin(14) #RIGHT WHEEL PWM
PD6 = machine.Pin(12) #RIGHT WHEEL PWM

#Some Previous Def
#PD7 = machine.Pin(13) #LEFT WHEEL PWM
#PD8 = machine.Pin(15)  #LEFT WHEEL PWM
#PD10 = machine.Pin(1)#,machine.Pin.OUT) #ENABLE PIN



pwmD5 = machine.PWM(PD5)
pwmD6 = machine.PWM(PD6)

#pwmD7 = machine.PWM(PD7)
#pwmD8 = machine.PWM(PD8)

pwmD5.freq(500) #Forward Pin Right
pwmD6.freq(500) #Backward Pin Right

#pwmD7.freq(500) #Forward Pin Left
#pwmD8.freq(500) #Backward Pin Left


pwmD5.duty(0)
pwmD6.duty(0)


Led = machine.Pin(2,machine.Pin.OUT) ## LED used to show the robot is Conneceted and functioning


