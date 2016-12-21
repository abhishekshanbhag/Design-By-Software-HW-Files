# AUTHOR Abhishek Shanbhag anshan@bu.edu
import sys
import numpy as np
#print("argc is",len(sys.argv))
for i,token in enumerate(sys.argv):
    print('argv of',i,'is',token)
x = sys.argv
argc = len(x)

def read_file(file_name, m, n, typ):
	mat_a = np.zeros((1,1))
	try:
		f = open(file_name)
	except:
		return 2, mat_a
	try:
		s_a = np.asarray((f.read()).split(), dtype=np.float)
		if(len(s_a) != m*n):
			return 3, mat_a
		else:
			if(typ == 'int'):
				for element in s_a:
					if(float(int(element)) != element):
						return 3, mat_a
			mat_a = np.resize(s_a, (m, n))		
		print(mat_a)
		f.close()	
		return 0,mat_a
	except:
		return 3, mat_a
	
def multiply_mat(a,b,m,l):
	c = np.zeros((m,l))
	b2 = np.transpose(b)
	try:
		for i in range(m):
			for k in range(l):
				c[i][k] = np.sum(np.multiply(a[i][:], b2[k][:]))
		#print(c)
		return 0, c
	except:
		return 4, c	

def write_file(file_name, c, typ):
	try:
		f = open(file_name, 'w')
		for i in range(c.shape[0]):
			line = ''
			for j in range(c.shape[1]):
				if(typ == 'double'):
					line = line + str(c[i][j]) + " "
				else:
					line = line + str(int(c[i][j])) + " "
			line = line + '\n'
			#print(line)
			f.write(line)
		f.close()
		return 0
	except:
		return 4	

def main():
	if((argc != 6) and (argc != 8)):
		#print(1)		
		exit(1)
	m = int(x[2])
	n = 0
	l = 0
	if(not((x[1] == "double") or (x[1] == "int"))):
		#print(1)		
		exit(1)
	if(m < 1):
		#print(1)
		exit(1)
	try:
		if(argc == 6):
				n = int(x[2])
				l = int(x[2])
				file_a = x[3]
				file_b = x[4]
				file_c = x[5]
		elif(argc == 8):
			n = int(x[3])
			l = int(x[4])
			if((n < 1) or (l < 1)):
				#print(1)
				exit(1)
			file_a = x[5]
			file_b = x[6]
			file_c = x[7]
	except:
		exit(1)
	ch,a = read_file(file_a, m, n, x[1])
	if(ch != 0):
		print(ch)
		exit(ch)
	ch,b = read_file(file_b, n, l, x[1])
	if(ch != 0):
		#print(ch)
		exit(ch)
	ch,c = multiply_mat(a,b, m, l)
	if(ch != 0):
		#print(ch)
		exit(ch)
	ch = write_file(file_c, c, x[1])
	if(ch != 0):
		#print(ch)
		exit(ch)
	#print(ch)
	exit(0)

if __name__ == '__main__':
	main()
