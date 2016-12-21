# AUTHOR hari chhari@bu.edu
import numpy as np
import scipy.io.wavfile as wavfile


# sleep while sound is playing
import time

# arrays
import numpy

import matplotlib.pyplot as pyplot





def dialer(file_name,frame_rate,phone,tone_time):
    #xarray = np.array([(941,1336),(607,1209),(697,1336),(697,1477),(770,1209),(770,1336),(770,1477),(852,1209),(852,1336),(852,1477)],dtype = np.float32)
    xarray = np.array([(941,1336),(697,1209),(697,1336),(697,1477),(770,1209),(770,1336),(770,1477),(852,1209),(852,1336),(852,1477)],dtype = np.int16)
    tone = []
    t = []   
    npoints = tone_time*frame_rate
    temp_t = np.zeros(npoints)   
    l = [int(g) for g in phone]
    for i in range(len(l)):
        temp_t= np.linspace(i*tone_time,(i+1)*tone_time,npoints, endpoint = False)
        print(temp_t)
        t = np.concatenate((t, temp_t))   
        print(len(t))
        tone = np.concatenate((tone,np.cos(2*np.pi*xarray[l[i]][0]*temp_t)+np.cos(2*np.pi*xarray[l[i]][1]*temp_t)))
    pyplot.plot(t[0:100], tone[0:100])
    pyplot.show()
    wavfile.write(file_name,frame_rate,tone)   
   
def main():
    dialer('321.wav',8000,'321',1)
   
if __name__ == '__main__':
    main()