import scipy.io.wavfile as wavfile
import numpy as np
#import matplotlib.pyplot as pyplot


def integral(signal, L, H):
	integral = np.sum(np.square(np.abs(signal[L:H+1])))
	return integral

def filter(signal, L, H, frame_rate):
	N = len(signal)
	new_sf = np.zeros(signal.shape, dtype=complex)
	new_sf[L:H+1] = signal[L:H+1]
	new_sf[N-H:N-L+1] = signal[N-H:N-L+1]
	return new_sf

def loudest_band(music, frame_rate, bandwidth):
	N = len(music)
	sf = np.fft.fft(music)
	sf = np.fft.fftshift(sf)
	t = np.linspace(0,N-1,N)
	maxl = 0
	maxh = 0
	max_val = 0
	L = (int(frame_rate/2)*int(N/frame_rate))
	H = (int(frame_rate/2) + bandwidth)*int(N/frame_rate)
	complete_flag = False
	while(complete_flag == False):
		x = integral(sf, L, H)
		if(x > max_val):
			max_val = x
			maxl = L
			maxh = H
		L += 1
		H += 1
		if(H > N-1):
			complete_flag = True
	new_sf = filter(sf, maxl, maxh, frame_rate)
	output = np.fft.ifftshift(new_sf)
	output = np.fft.ifft(output)
	return maxl, maxh, output

def main():
	#frame_rate, music = wavfile.read("bach10sec.wav")
	#print(music.shape)
	#loudest(music[:,0], frame_rate, 100)
	pass

if __name__ == '__main__':
	main()
