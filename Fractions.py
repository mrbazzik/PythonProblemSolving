def gcd(a, b):
	while a % b != 0:
		olda = a
		oldb = b
		a = oldb
		b = olda%oldb
	return b
class Fraction:
	def __init__(self, num, den):
		self.num = num
		self.den = den
	def __add__(self, fraction):
		num = self.num*fraction.den+self.den*fraction.num
		den = self.den*fraction.den
		com = gcd(num, den)
		return Fraction(num/com, den/com)
	def __eq__(self, fraction):
		selfnum = self.num*fraction.den
		num = fraction.num*self.den
		return selfnum == num
	def __lt__(self, fraction):
		selfnum = self.num*fraction.den
		num = fraction.num*self.den
		return selfnum < num
	def __gt__(self, fraction):
		selfnum = self.num*fraction.den
		num = fraction.num*self.den
		return selfnum > num
	def __le__(self, fraction):
		return self.__eq__(fraction) | self.__lt__(fraction)
	def __ge__(self, fraction):
		return self.__eq__(fraction) | self.__gt__(fraction)
	def __mul__(self, fraction):
		num = self.num*fraction.num
		den = self.den*fraction.den
		com = gcd(num, den)
		return Fraction(num/com, den/com) 
	def __div__(self, fraction):
		num = self.num*fraction.den
		den = self.den*fraction.num
		com = gcd(num, den)
		return Fraction(num/com, den/com) 
	def __sub__(self, fraction):
		num = self.num*fraction.den-self.den*fraction.num
		den = self.den*fraction.den
		com = gcd(num, den)
		return Fraction(num/com, den/com)
	def __str__(self):
		return str(self.num)+"/"+str(self.den)

a = Fraction(1, 3)
b = Fraction(3, 4)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a==b)
print(a>b)
print(a<b)