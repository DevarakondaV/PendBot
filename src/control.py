import machine
import time
import micropython
#from Icom import *
micropython.alloc_emergency_exception_buf(100)
"""
""This file defines the functions and variables responsible for complete control of the robot.
""
""
"""

#Some Functions

"""
"" Moves Robot forward or backward
"" if dcycle<0 move backwards dycle>0 move forward
"""
def moveRobot(dcycle):
    global pwmD5    #Forwad Pin right
    global pwmD6    #Backward Pin Right
    global o_dots
    global mss

    tim = machine.Timer(-1)
    tim.init(period=100,mode=machine.Timer.PERIODIC,callback=ang_vel)

    if dcycle < 0:
        dcycle = abs(dcycle)
        pwmD5.duty(0)
        pwmD6.duty(dcycle)
    else:
        pwmD5.duty(dcycle)
        pwmD6.duty(0)

    #Will run for 3 seconds and Write to File with the name dcycle
    #write_to_file(dcycle)

    ms_lim = time.ticks_ms()
    po = 0
    while(ms_lim+3000 > time.ticks_ms()):
        po = po+1
    #After 5 seconds. Return robot to standstill
    pwmD5.duty(0)
    pwmD6.duty(0)
    
    tim.deinit()


    #f = open(str(dcycle)+".txt","w")
    #for i in range(len(o_dots)):
        #f.write(str(mss[i])+"\t"+str(o_dots)+"\n")

    #f.close()
    ms = 0
    

    
"""
"" Pin Interrump
"""
def interrupt_callback(p):
    global pulse
    pulse = pulse + 1

"""
"" Angular velocity Calc
"""
def ang_vel(tmr):
    global pulse
    global o_dot
    global ms

    #o_dot = ((pulse<<2)*3.14)/20.0
    ms = ms+1
    o_dot = (3.14*pulse)
    print(ms,o_dot)
    pulse = 0

"""
"" Deactivate pwm Pins
"""
def DeactivatePins():
    global pwmD5
    global pwmD6

    pwmD5.deinit()
    pwmD6.deinit()





"""
"" Flashes Built in LED ntimes to define certain actions taken
"" 
"" Number of flashes -> Definition
"" 2 Flashes -> I2C device not recognized.
"" 3 Flashes -> I2C device recognized and connected
"" 4 Flashes -> Connected to Internet
"""
def flash_led(ntimes):
    global Led
    
    while ntimes > 0:
        Led.low()
        time.sleep_ms(500)
        Led.high()
        ntimes = ntimes-1

"""
"" Function prints accel readings
"""
def print_accel(ml):
    global AcXoffset, AcYoffset, AcZoffset, GyXoffset, GyYoffset, GyZoffset
    global accel


    cfac = 16384
    while(True):
        time.sleep_ms(ml)
        vals = accel.get_values()
        AcX = vals["AcX"]-AcXoffset
        AcY = vals["AcY"]-AcYoffset
        AcZ = vals["AcZ"]-AcZoffset
        GyX = vals["GyX"]-GyXoffset
        GyY = vals["GyY"]-GyYoffset
        GyZ = vals["GyZ"]-GyZoffset

        AcX = AcX/cfac
        AcY = AcY/cfac
        AcZ = AcZ/cfac
        GyX = GyX/131
        GyY = GyY/131
        GyZ = GyZ/131

        print("AcX: {:5.3f}\tAcY: {:5.3f}\tAcZ: {:5.3f}\tGyX: {:5.3f}\tGyY: {:5.3f}\tGyZ: {:5.3f}".format(AcX,AcY,AcZ,GyX,GyY,GyZ))



#############################################################################################
#Pin definitions for PWM and Led
#Defining pins for pwm
PD5 = machine.Pin(14) #RIGHT WHEEL PWM
PD6 = machine.Pin(12) #RIGHT WHEEL PWM
PD7 = machine.Pin(13,machine.Pin.IN) #WHEEL SENSOR
PD7.irq(trigger=machine.Pin.IRQ_FALLING,handler=interrupt_callback)

pwmD5 = machine.PWM(PD5)
pwmD6 = machine.PWM(PD6)

pwmD5.freq(500) #Forward Pin Right
pwmD6.freq(500) #Backward Pin Right

pwmD5.duty(0)
pwmD6.duty(0)


Led = machine.Pin(2,machine.Pin.OUT) ## LED used to show the robot is Conneceted and functioning
Led.off()
##############################################################################################


##############################################################################################
#I2C Communication Defintions
#I2C com 
#i2c = machine.I2C(scl=machine.Pin(4),sda=Pin(5),freq=100000)
#I2C Address
#i2cDevicesAddr = i2c.scan()

## IF there are no I2C devices,
## Flash LED twice and exit program
#if (len(i2cDevicesAddr) == 0):
#    flash_led(2)
#else:
#    accAddr = i2cDevicesAddr[0]
#    flash_led(3)

# accelerometer class
#accel = acc(i2c,accAddr)
AcZoffset = 748.4766
AcXoffset = -291.7535
AcYoffset = -227.5296
GyXoffset = -334.9083
GyYoffset = 139.0406
GyZoffset = 78.57318
##############################################################################################


##############################################################################################
#Some variables
pulse = 0
o_dot = 0
ms = 0
o_dots = []
mss = []
#Timer
#tim = machine.Timer(-1)
#tim.init(period=100,mode=machine.Timer.PERIODIC,callback=ang_vel)

