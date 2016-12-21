# AUTHOR Vrushali M vmahajan@bu.edu

import numpy as np

x_of_n = input().split(' ')
h_of_n = input().split(' ')

for i in range(len(x_of_n)):
	x_of_n[i] = float(x_of_n[i])
for i in range(len(h_of_n)):
	h_of_n[i] = float(h_of_n[i])

y = np.convolve(x_of_n,h_of_n)
j = []
for i in range(len(y)):
	j.append(str(y[i]))

s = ' '


print(s.join(j))



