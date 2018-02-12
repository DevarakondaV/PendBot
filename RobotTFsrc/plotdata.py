#This file will plot the data recorded from accelerometer
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import numpy as np


#Files Director
files_dir = "/home/vishnu/Documents/EngProjs/PendBot/PendBot/Data/AccelData"



#Defining some functions

"""
"" Splits words/values from strg(string) and returns into indexed array
"""
def split_raw_string(strg):
    addstr = ""
    rtnlist = []
    for idx in range(len(strg)):
        if strg[idx].isdigit() or strg[idx] is '.':
            addstr = addstr+strg[idx]
        else:
            if addstr is not "":
                rtnlist.append(addstr)
            addstr = ""
        idx = idx+1

    rtnMap = {'Dcycle': float(rtnlist[0]) ,'Tstamp': float(rtnlist[1]),'Ax': float(rtnlist[2]),'Ay': float(rtnlist[3]),'Az': float(rtnlist[4])}
    
    return rtnMap

"""
"" Reads the contents of the file in path and splits the values into seperate arrays for each component of acceleration
"""
def read_files_into_array(path): 

    dcycle = ""
    for val in path:
        if val.isdigit():
            dcycle = dcycle+val

 
    
    rtnMap = {'Dcycle': 0,'Tstamp': [],'Ax': [],'Ay': [],'Az': []}
    rtnMap['Dcycle'] = int(dcycle)

    with open(path,'r') as fp:
        
        for i in range(0,10):
            line = fp.readline()
        
        while line:
            #print(line)
            data = split_raw_string(line)
            #print(data)
            line = fp.readline()
            line = fp.readline()

            rtnMap['Tstamp'].append(data['Tstamp'])
            rtnMap['Ax'].append(data['Ax'])
            rtnMap['Ay'].append(data['Ay'])
            rtnMap['Az'].append(data['Az'])
        
        
    return rtnMap
        


"""
"" Function prints raw strings from file at path
"""
def print_file(path):
    with open(path,'r') as fp:
        line = fp.readline()
        while line:
            print repr(line)
            line = fp.readline()





TestLine = '300\t\t1231\t\t-0.011\t\t0.111\t\t1.694\r\n'

#print_file(files_dir+"/800.txt")
#v = split_raw_string(TestLine)
#print(v)


data300 = read_files_into_array(files_dir+"/300.txt")
data340 = read_files_into_array(files_dir+"/340.txt")
data380 = read_files_into_array(files_dir+"/380.txt")
data420 = read_files_into_array(files_dir+"/420.txt")
data460 = read_files_into_array(files_dir+"/460.txt")
data500 = read_files_into_array(files_dir+"/500.txt")
data540 = read_files_into_array(files_dir+"/540.txt")
data600 = read_files_into_array(files_dir+"/600.txt")
data640 = read_files_into_array(files_dir+"/640.txt")
data680 = read_files_into_array(files_dir+"/680.txt")
data720 = read_files_into_array(files_dir+"/720.txt")
data700 = read_files_into_array(files_dir+"/700.txt")
data800 = read_files_into_array(files_dir+"/800.txt")
data840 = read_files_into_array(files_dir+"/840.txt")
data880 = read_files_into_array(files_dir+"/880.txt")
data920 = read_files_into_array(files_dir+"/920.txt")
data960 = read_files_into_array(files_dir+"/960.txt")
data1000 = read_files_into_array(files_dir+"/1000.txt")
data1040 = read_files_into_array(files_dir+"/1040.txt")
data1080 = read_files_into_array(files_dir+"/1080.txt")
data1120 = read_files_into_array(files_dir+"/1120.txt")
data1160 = read_files_into_array(files_dir+"/1160.txt")




dcycle = data1000['Dcycle']
Tstamp = np.array(data1000['Tstamp'])
Ax = np.array(data1000['Ax'])
Ay = np.array(data1000['Ay'])
Az = np.array(data1000['Az'])


#print(Ax)
#print(Ay)
#print(Az)


#Filter definitions

n = 10
b = [1.0 / n]*n
a = 1
Ax = lfilter(b,a,Ax)
Ay = lfilter(b,a,Ay)
Az = lfilter(b,a,Az)


"""
Ax = np.polyfit(Tstamp,Ax,5)
Ay = np.polyfit(Tstamp,Ay,5)
Az = np.polyfit(Tstamp,Az,5)


fnAx = np.poly1d(Ax)
fnAy = np.poly1d(Ay)
fnAz = np.poly1d(Az)

#Tstamp = np.arange(1,3,.001)
#print(Tstamp)
Ax = fnAx(Tstamp)
Ay = fnAy(Tstamp)
Az = fnAz(Tstamp)
"""

plt.subplots(ncols=1,nrows=3)
plt.subplot(311)
#plt.plot(Tstamp,Ax,'bo', label="Ax")
plt.plot(Tstamp,Ax)
plt.subplot(312)
#plt.plot(Tstamp,Ay,'go', label="Ay")
plt.plot(Tstamp,Ay)
plt.subplot(313)
#plt.plot(Tstamp,Az,'ro', label="Az")
plt.plot(Tstamp,Az)
plt.legend()

plt.show()

