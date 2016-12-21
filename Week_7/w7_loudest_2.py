import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as pyplot

def init_band(frame_rate, bandwidth):
	L = int(frame_rate/2)
	H = int(frame_rate/2) + (bandwidth - 1)
	return H,L


def loudest(music, frame_rate, bandwidth):
	xk = np.fft.fft(music)
	N = len(music)
	print(xk)
	t = np.linspace(-np.pi,np.pi, N, endpoint = False)
	print(len(xk))
	pyplot.plot(t,np.abs(xk))
	pyplot.show()
	print(xk[int(len(xk)/2)])
	xk = np.fft.fftshift(xk)
	print(xk)
	pyplot.plot(t,np.abs(xk))
	pyplot.show()
	print(xk[int(len(xk)/2)])
	low_k = int(N/2)
	H, L = init_band(frame_rate, bandwidth)
	

def main():
	frame_rate, music = wavfile.read("bach10sec.wav")
	loudest(music[:,0], frame_rate, 100)

if __name__ == '__main__':
	main()
