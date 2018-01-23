"""
Source
Based on github user: adamjezek98 
Repo: MPU6050-esp8266-MicroPython
url: https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython.git
"""
from machine import Pin,I2C

class acc():

    #Constructor
    def __init__(self, i2c, addr):
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        self.iic.writeto(self.addr,bytearray([107,0]))
        self.iic.stop()


    #Grabs Raw values from MPU6050
    def get_raw_values(self):
        self.iic.start()
        ready = 0
        while not ready:
            ready = self.iic.readfrom_mem(self.addr,0x3A,1)[0]
            ready = (ready & 1)
        a = self.iic.readfrom_mem(self.addr,0x3B,14)
        self.iic.stop()
        return a

    #Gets Values in raw array
    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    # Converts the bytes to 16bit ints
    def bytes_toint(self,firstbyte,secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255)+1)

    # Returns values in a map
    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0],raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2],raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4],raw_ints[5])
        vals["Tmp"] = self.bytes_toint(raw_ints[6],raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8],raw_ints[9])
        vals["GyY"] = self.bytes_toint(raw_ints[10],raw_ints[11])
        vals["GyZ"] = self.bytes_toint(raw_ints[12],raw_ints[13])
        return vals


    def val_test(self): #ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)


