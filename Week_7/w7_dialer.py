# AUTHOR Abhishek Shanbhag anshan@bu.edu
# AUTHOR Hari chhari@bu.edu
# AUTHOR Ameya Apastamb ameyama@bu.edu
# AUTHOR Shreyas joshi svmjoshi@bu.edu

import scipy.io.wavfile as wavfile
import numpy as np
from numpy import array

def dialer(file_name, frame_rate, phone, tone_time):
	freq = {"1": [1209,697], "2": [1336,697], "3": [1477,697], "4": [1209,770], "5": [1336,770], "6": [1477,770], "7": [1209,852], "8": [1336,852], "9": [1477,852], "0": [1336,941]}
	#try:
	soundwave = np.array([])
	#print(soundwave.shape)
	#print(soundwave.size)
	#print(soundwave)
	t = np.linspace(0,tone_time, frame_rate*tone_time)
	for i in phone:
		freq_for_num = freq[i]
		y = np.add(np.sin((2*np.pi*freq_for_num[0]*t)),np.sin((2*np.pi*freq_for_num[1]*t)))
		#print(y.shape)
		#print(y.size)
		#print(y)
		soundwave = np.append(soundwave,y)
	#print(soundwave)
	wavfile.write(file_name, frame_rate, soundwave)

def main():
	#dialer("Sound_1.wav", 44100, "1", 2)
	pass
if __name__ == '__main__':
	main()
