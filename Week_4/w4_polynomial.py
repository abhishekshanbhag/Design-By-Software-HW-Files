# AUTHOR Abhishek Shanbhag anshan@bu.edu
# AUTHOR Ziteng Xu zxu83@bu.edu
class Polynomial():
	def __init__(self, sequence = []):
		self.sequence = dict({})
		for i in range(len(sequence)):
			if(sequence[i] != 0):
				self.sequence.update({len(sequence) - 1 - i:sequence[i]})
		#self.max = len(sequence) - 1
		#self.min = 0
		#print("Created new Polynomial with sequence: " + str(self.sequence))
		#print("Max Power = " + str(self.max))
		#print("Min Power = " + str(self.min))
	
	def __str__(self):
		poly = ""
		s = list(reversed(sorted(self.sequence)))
		for i in s:
			if((i > 1) or (i < 0)):
				poly += "%sx^%d" %(str(self.sequence[i]), i)
			elif(i == 1):
				poly += "%sx" %(str(self.sequence[i]))
			else:
				poly += "%s" %(str(self.sequence[i]))
			if(i != min(s)):
				poly += " + "
		return poly

	def __repr__(self):
		poly = ""
		s = list(reversed(sorted(self.sequence)))
		for i in s:
			if((i > 1) or (i < 0)):
				poly += "%sx^%d" %(str(self.sequence[i]), i)
			elif(i == 1):
				poly += "%sx" %(str(self.sequence[i]))
			else:
				poly += "%s" %(str(self.sequence[i]))
			if(i != min(s)):
				poly += " + "
		return poly

	def __setitem__(self, k, v):
		if(v != 0):
			self.sequence.update({k:v})
			print("Added item. Sequence is now: " + str(self.sequence))
			"""if(k > self.max):
				self.max = k
				print("Max changed to: "+ str(self.max))
			if(k < self.min):
				self.min = k
				#print("Min changed to: " + str(self.min))"""
		else:
			print("Not added item as value of coefficient is 0.")
	
	def __getitem__(self, key):
		if key in self.sequence:
			return self.sequence[key]
		else:
			return 0


	def __add__(self, poly):
		sum_poly = Polynomial([0])
		"""if(self.max > poly.max):
			sum_poly.max = self.max
		else:
			sum_poly.max = poly.max
		if(self.min < poly.min):
			sum_poly.min = self.min
		else:
			sum_poly.min = poly.min"""
		#print("Max in Sum: "+str(sum_poly.max))
		#print("Min in Sum: "+str(sum_poly.min))		
		for i in self.sequence:
			if (i in poly.sequence):
				sum_poly.sequence[i] = (self.sequence[i] + poly.sequence[i])
			else:
				sum_poly.sequence[i] = self.sequence[i]
		for i in poly.sequence:
			if not(i in self.sequence):
				sum_poly.sequence[i] = poly.sequence[i]
		return sum_poly

	"""def __radd__(self, poly):
		sum_poly = Polynomial([0])
		if(self.max > poly.max):
			sum_poly.max = self.max
		else:
			sum_poly.max = poly.max
		if(self.max < poly.max):
			sum_poly.min = self.min
		else:
			sum_poly.min = poly.min
		#print("Max in Sum: "+str(sum_poly.max))
		#print("Min in Sum: "+str(sum_poly.min))
		for i in self.sequence:
			if (i in poly.sequence):
				sum_poly.sequence[i] = (self.sequence[i] + poly.sequence[i])
			else:
				sum_poly.sequence[i] = self.sequence[i]
		for i in poly.sequence:
			if not(i in self.sequence):
				sum_poly.sequence[i] = poly.sequence[i]
		return sum_poly"""

	def __sub__(self, poly):
		sum_poly = Polynomial([0])
		"""if(self.max > poly.max):
			sum_poly.max = self.max
		else:
			sum_poly.max = poly.max
		if(self.min < poly.min):
			sum_poly.min = self.min
		else:
			sum_poly.min = poly.min"""
		#print("Max in Sum: "+str(sum_poly.max))
		#print("Min in Sum: "+str(sum_poly.min))
		for i in self.sequence:
			if (i in poly.sequence):
				sum_poly.sequence[i] = (self.sequence[i] - poly.sequence[i])
			else:
				sum_poly.sequence[i] = self.sequence[i]
		for i in poly.sequence:
			if not(i in self.sequence):
				sum_poly.sequence[i] = -poly.sequence[i]
		return sum_poly

	def __rsub__(self, poly):
		sum_poly = Polynomial([0])
		"""if(self.max > poly.max):
			sum_poly.max = self.max
		else:
			sum_poly.max = poly.max
		if(self.min < poly.min):
			sum_poly.min = self.min
		else:
			sum_poly.min = poly.min"""
		#print("Max in Sum: "+str(sum_poly.max))
		#print("Min in Sum: "+str(sum_poly.min))
		for i in self.sequence:
			if (i in poly.sequence):
				sum_poly.sequence[i] = (poly.sequence[i] - self.sequence[i])
			else:
				sum_poly.sequence[i] = -self.sequence[i]
		for i in poly.sequence:
			if not(i in self.sequence):
				sum_poly.sequence[i] = poly.sequence[i]
		return sum_poly
	
	def __eq__(self, poly):
		try:
			if(len(self.sequence) == len(poly.sequence)):
				for i in self.sequence:
					if(self.sequence[i] != poly.sequence[i]):
						return False
				return True
			else:
				return False
		except:
			return False
	def deriv(self):
		der = Polynomial()
		for i in self.sequence:
			if(i != 0):
				der.sequence[i - 1] = self.sequence[i]*i
		"""if(self.max != 0):
			der.max = self.max - 1
		if(self.min != 0):
			der.min = self.min - 1"""
		return der

	def __mul__(self, poly):
		mul_poly = Polynomial()
		for i in self.sequence:
			for j in poly.sequence:
				if((i + j) in mul_poly.sequence):
					mul_poly.sequence[i+j] += (self.sequence[i] * poly.sequence[j])
				else:
					mul_poly.sequence[i+j] = (self.sequence[i] * poly.sequence[j])
				"""if((i+j) > mul_poly.max):
					mul_poly.max = (i+j)
				if((i+j) < mul_poly.min):
					mul_poly.min = (i-j)"""
			
		return mul_poly

	def eval(self, val):
		sum = 0
		for i in self.sequence:
			sum += self.sequence[i]*(val**i)
		return sum


def main():
	x = Polynomial()
	print(str(x))
	x[-5] = 6
	x[3] = complex(2,4)
	print(str(x))
	
	y = Polynomial([5,-4,complex(6,4),6,2,-1])
	z = x+y
	print(str(z))
	print(z)
	print(str(x))
	z = y+x
	print(str(x))
	print(str(x[-5]))
	pass

if __name__ == '__main__':
	main()
