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
    plen = len(path)
    dcycle = path[plen-7:plen-4]
    
    rtnMap = {'Dcycle': 0,'Tstamp': [],'Ax': [],'Ay': [],'Az': []}
    rtnMap['Dcycle'] = int(dcycle)

    with open(path,'r') as fp:
        for i in range(0,10):
            line = fp.readline()
        
        while line:
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





TestLine = '300\t\t0.1\t\t-0.011\t\t0.111\t\t1.694\r\n'

#print_file(files_dir+"/300.txt")
#v = split_raw_string(TestLine)
data300 = read_files_into_array(files_dir+"/300.txt")
data340 = read_files_into_array(files_dir+"/340.txt")
data380 = read_files_into_array(files_dir+"/380.txt")
data420 = read_files_into_array(files_dir+"/420.txt")
data460 = read_files_into_array(files_dir+"/460.txt")
data500 = read_files_into_array(files_dir+"/500.txt")
data540 = read_files_into_array(files_dir+"/540.txt")
data580 = read_files_into_array(files_dir+"/580.txt")
data620 = read_files_into_array(files_dir+"/620.txt")
data660 = read_files_into_array(files_dir+"/660.txt")
data700 = read_files_into_array(files_dir+"/700.txt")
data740 = read_files_into_array(files_dir+"/740.txt")
data780 = read_files_into_array(files_dir+"/780.txt")
data820 = read_files_into_array(files_dir+"/820.txt")
data860 = read_files_into_array(files_dir+"/860.txt")
data900 = read_files_into_array(files_dir+"/900.txt")
data940 = read_files_into_array(files_dir+"/940.txt")
data980 = read_files_into_array(files_dir+"/980.txt")
data999 = read_files_into_array(files_dir+"/999.txt")
data1000 = read_files_into_array(files_dir+"/1000.txt")

dcycle = data740['Dcycle']
Tstamp = np.array(data1000['Tstamp'])
Ax = np.array(data1000['Ax'])
Ay = np.array(data1000['Ay'])
Az = np.array(data1000['Az'])


#Filter definitions
n = 25
b = [1.0 / n]*n
a = 1
Ax = lfilter(b,a,Ax)
Ay = lfilter(b,a,Ay)
Az = lfilter(b,a,Az)



"""
Ax = np.polyfit(Tstamp,Ax,10)
Ay = np.polyfit(Tstamp,Ay,10)
Az = np.polyfit(Tstamp,Az,10)


fnAx = np.poly1d(Ax)
fnAy = np.poly1d(Ay)
fnAz = np.poly1d(Az)


Ax = fnAx(Tstamp)
Ay = fnAy(Tstamp)
Az = fnAz(Tstamp)
"""
plt.subplots(ncols=1,nrows=3)
plt.subplot(311)
#plt.plot(Tstamp,Ax,'ro', label="Ax")
plt.plot(Tstamp,Ax)
plt.subplot(312)
#plt.plot(Tstamp,Ay,'ro', label="Ay")
plt.plot(Tstamp,Ay)
plt.subplot(313)
#plt.plot(Tstamp,Az,'ro', label="Az")
plt.plot(Tstamp,Az)
plt.legend()

plt.show()

