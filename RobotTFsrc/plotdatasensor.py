"""
This file plots input data taken using the photoresistor and Led
"""
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import numpy as np



#Files Director
files_dir = "/home/vishnu/Documents/EngProjs/PendBot/PendBot/Data/AngAccelData"


"""
Finds the numberical values inside the file for second and photoresistor voltage and
returns array with contents.
"""
def read_data_lines(path):
    sec = "Seconds:" 
    PhotoRVol = "PhotoResistor Voltage:"

    rtnMap = {"seconds": [],"voltage": []}
    
    with open(path,'r') as fp:

        line = fp.readline()
        while line:
            line = fp.readline()
            if (line.find(sec) is not -1 and line.find(PhotoRVol) is not -1):
                #print(line)
                sec_idx = len(sec)+1
                PhotoRVol_idx = line.find(PhotoRVol)+len(PhotoRVol)+1
                
                seconds = int(line[sec_idx:sec_idx+2])
                PRVvoltage = int(line[PhotoRVol_idx:PhotoRVol_idx+4])
                
                
                if len(str(seconds)) is not 2:
                    rtnMap["seconds"].append(seconds)
                    rtnMap["voltage"].append(PRVvoltage)
    
    return rtnMap



data400 = read_data_lines(files_dir+"/400.txt")
data500 = read_data_lines(files_dir+"/500.txt")
#data600 = read_data_lines(files_dir+"/600.txt")
#data700 = read_data_lines(files_dir+"/700.txt")
#data800 = read_data_lines(files_dir+"/800.txt")
#data900 = read_data_lines(files_dir+"/900.txt")
data1000 = read_data_lines(files_dir+"/1000.txt")
#dataAll = read_data_lines(files_dir+"/All.txt")




secs = data400["seconds"];
print(secs.count(0));
print(secs.count(1));
print(secs.count(2));
print(secs.count(3));


v400 = data400['voltage']
v500 = data500['voltage']
v1000 = data1000['voltage']

t400 = np.arange(0,len(v400))
t500 = np.arange(0,len(v500))
t1000 = np.arange(0,len(v1000))

v400 = np.array(v400)
v500 = np.array(v500)
v1000 = np.array(v1000)


plt.subplots(ncols=1,nrows=3)
plt.subplot(3,1,1)
plt.plot(t400,v400)
plt.subplot(3,1,2)
plt.plot(t500,v500)
plt.subplot(3,1,3)
plt.plot(t1000,v1000)
plt.show()

