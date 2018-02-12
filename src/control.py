import machine
import time
from Icom import *
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
""This file defines the functions and variables responsible for complete control of the robot.
""
""
"""

#Some Functions

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
"" Moves Robot forward or backward
"" if dcycle<0 move backwards dycle>0 move forward
"""
def moveRobot(dcycle):
    global pwmD5    #Forwad Pin right
    global pwmD6    #Backward Pin Right
    

    if dcycle < 0:
        dcycle = abs(dcycle)
        pwmD5.duty(0)
        pwmD6.duty(dcycle)
    else:
        pwmD5.duty(dcycle)
        pwmD6.duty(0)

    #Will run for 3 seconds and Write to File with the name dcycle
    #write_to_file(dcycle)


    ms = time.ticks_ms();
    ms = ms+3000;
    po = 0
    while(ms > time.ticks_ms()):
        po = po+1
    
    #After 3 seconds. Return robot to standstill
    pwmD5.duty(0)
    pwmD6.duty(0)



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
"" Writes data values to file with filename
""
"""
def write_to_file(FileName):
    global Led
    global accel
    global AcXoffset, AcYoffset, AcZoffset, GyXoffset, GyYoffset, GyZoffset
    global pwmD5, pwmD6

    #Lighting the Led
    Led.low()

    #Preparing File to Read
    f = open(str(FileName)+".txt",'w')
    f.write("#############################################################################################\n")
    f.write("File Contains Acceleration Data\n")
    f.write("Accelerations are given as a multiple of g\n")
    f.write("------------------------------------------\n")
    f.write("First line is duty cycle\n")
    f.write("Second line is time stamp\n")
    f.write("Rest are accelerations\n")
    f.write("#############################################################################################\n")
    f.write("Dcycle\t\tTimeStamp\t\tAx\t\tAy\t\tAz\n")


    aconv = 16384 #Conversion factor for readings for accelerometer
    #Read for 3 seconds

    ms = time.ticks_ms()
    t = 0
    while(ms+1000 > time.ticks_ms()):
        readings = accel.get_values()


        Ax = readings['AcX']-AcXoffset
        Ay = readings['AcY']-AcYoffset
        Az = readings['AcZ']-AcZoffset

        Ax = Ax/aconv
        Ay = Ay/aconv
        Az = Az/aconv

        write_val = str(FileName)+"\t\t"+str(time.ticks_ms()-t)+"\t\t{:5.3f}\t\t{:5.3f}\t\t{:5.3f}\n".format(Ax,Ay,Az)+"\n"

        f.write(write_val)
        t = t+1


    if FileName < 0:
        dcycle = abs(FileName)
        pwmD5.duty(0)
        pwmD6.duty(FileName)
    else:
        pwmD5.duty(FileName)
        pwmD6.duty(0)
    ms = time.ticks_ms()
    
    while(ms+1000 > time.ticks_ms()):

        readings = accel.get_values()
        Ax = readings['AcX']-AcXoffset
        Ay = readings['AcY']-AcYoffset
        Az = readings['AcZ']-AcZoffset

        Ax = Ax/aconv
        Ay = Ay/aconv
        Az = Az/aconv

        write_val = str(FileName)+"\t\t"+str(time.ticks_ms()-t)+"\t\t{:5.3f}\t\t{:5.3f}\t\t{:5.3f}\n".format(Ax,Ay,Az)+"\n"
        f.write(write_val)
        t = t+1
       
    pwmD5.duty(0)
    pwmD6.duty(0)

    ms = time.ticks_ms()
    while(ms+1000 > time.ticks_ms()):

        readings = accel.get_values()
        Ax = readings['AcX']-AcXoffset
        Ay = readings['AcY']-AcYoffset
        Az = readings['AcZ']-AcZoffset

        Ax = Ax/aconv
        Ay = Ay/aconv
        Az = Az/aconv

        write_val = str(FileName)+"\t\t"+str(time.ticks_ms()-t)+"\t\t{:5.3f}\t\t{:5.3f}\t\t{:5.3f}\n".format(Ax,Ay,Az)+"\n"
        f.write(write_val)
        t = t+1

    f.close()
    #Turing Led off
    Led.high()


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




"""
"This function calibrates the gyro and accel offset. Only need to run once and store values returned
"""
def calibrate_accel():
    global accel
    rtnvals = {}
    
    N = 1 #Sample Size
    AvgAcX = 0
    AvgAcY = 0
    AvgAcZ = 0
    AvgGyX = 0
    AvgGyY = 0
    AvgGyZ = 0
    while N < 5000:
        vals = accel.get_values()
        nAcX = vals["AcX"] 
        nAcY = vals["AcY"]
        nAcZ = vals["AcZ"]
        nGyX = vals["GyX"]
        nGyY = vals["GyY"]
        nGyZ = vals["GyZ"]

        AvgAcX = AvgAcX + nAcX
        AvgAcY = AvgAcY + nAcY
        AvgAcZ = AvgAcZ + nAcZ
        AvgGyX = AvgGyX + nGyX
        AvgGyY = AvgGyY + nGyY
        AvgGyZ = AvgGyZ + nGyZ
        N = N+1

    AvgAcX = AvgAcX/N
    AvgAcY = AvgAcY/N
    AvgAcZ = AvgAcZ/N
    AvgGyX = AvgGyX/N
    AvgGyY = AvgGyY/N
    AvgGyZ = AvgGyZ/N

    
    setGyroXoffset = AvgGyX
    setGyroYoffset = AvgGyY
    setGyroZoffset = AvgGyZ
    setAccXoffset = AvgAcX
    setAccYoffset = AvgAcY
    setAccZoffset = -16364+AvgAcZ

    rtnVal = {"GyXoffset": setGyroXoffset,"GyYoffset": setGyroYoffset, "GyZoffset": setGyroZoffset,
            "AcXoffset": setAccXoffset, "AcYoffset": setAccYoffset, "AcZoffset": setAccZoffset}

    return rtnVal


#############################################################################################
#Pin definitions for PWM and Led
#Defining pins for pwm
PD5 = machine.Pin(14) #RIGHT WHEEL PWM
PD6 = machine.Pin(12) #RIGHT WHEEL PWM

pwmD5 = machine.PWM(PD5)
pwmD6 = machine.PWM(PD6)

pwmD5.freq(500) #Forward Pin Right
pwmD6.freq(500) #Backward Pin Right

pwmD5.duty(0)
pwmD6.duty(0)


Led = machine.Pin(2,machine.Pin.OUT) ## LED used to show the robot is Conneceted and functioning
Led.low()
##############################################################################################


##############################################################################################
#I2C Communication Defintions
#I2C com 
i2c = machine.I2C(scl=machine.Pin(4),sda=Pin(5),freq=100000)
#I2C Address
i2cDevicesAddr = i2c.scan()

## IF there are no I2C devices,
## Flash LED twice and exit program
if (len(i2cDevicesAddr) == 0):
    flash_led(2)
else:
    accAddr = i2cDevicesAddr[0]
    flash_led(3)

# accelerometer class
accel = acc(i2c,accAddr)
AcZoffset = 748.4766
AcXoffset = -291.7535
AcYoffset = -227.5296
GyXoffset = -334.9083
GyYoffset = 139.0406
GyZoffset = 78.57318
##############################################################################################
