import os

def baseConverter(ibase,obase,inum,bases):
	negNum = 0
	if inum.find('-') == 0:
		negNum = 1
	else:
		pass

	for n in list(inum):
		if not bases.has_key(n) or bases[n] >= ibase:
			if n != '.' and n != '-':
				print "Invalid Number."
				exit()

	if inum.find('.') == -1:
		inum = inum + '.0'
		
	if negNum == 1:
		inum = inum[1:]
	intPart = list(inum.split('.')[0])
	fracPart = list(inum.split('.')[1])

	decSum = 0
	count = 0
	intPart.reverse()
	for i in intPart:
		decSum = decSum+(bases[i]*(ibase**count))
		count = count + 1

	fracSum = 0.0
	count = -1
	for i in fracPart:
		fracSum = fracSum+(bases[i]*ibase**count)
		count = count - 1

	bases = dict((v,k) for k,v in bases.iteritems())
	
	#print bases
	onum = []
	while decSum > 0:
		onum.append(bases[int(decSum%obase)])
		decSum = decSum / obase
	if negNum == 1:
		onum.append('-')
	onum.reverse()

	if fracSum != 0.0:
		count = 0
		onum.append('.')
		while count<10:
			fracSum = fracSum*obase
			fr = int(fracSum)
			if fr != 0:
				onum.append(bases[fr])
				fracSum = fracSum - fr
			count = count + 1			

	return float(''.join(onum))

def performOperation(num1,num2,op):
	if op == '+':
		return num1 + num2
	elif op == '-':
		return num1 - num2
	elif op == '|':
		return int(num1) | int(num2)
	elif op == '&':
		return int(num1) & int(num2)

def main():
	bases=dict()
	for i in range(10):
		bases[str(i)] = i
	for i in range(65,91):
		bases[chr(i)] = i-55
	for i in range(97,123):
		bases[chr(i)] = i-61
	#print bases
	os.system('clear')
	base1 = raw_input("Enter Base 1: ")
	if not base1.isdigit():
		print "Invalid Base"
		exit()
	num1 = raw_input("Enter first number (in base %s): "%base1)
	num1 = baseConverter(int(base1),10,num1,bases)
	print num1

	base2 = raw_input("Enter Base 2: ")
	if not base2.isdigit():
		print "Invalid Base"
		exit()
	num2 = raw_input("Enter second number (in base %s): "%base2)
	num2 = baseConverter(int(base2),10,num2,bases)
	print num2

	validOp = ['+','-','&','|']
	op = raw_input('Enter a symbol (+ = Add  - = Subtract(1-2)  & = Logical And  | = Logical Or): ')
	if op not in validOp:
		print 'Invlid Operand'
		exit()

	result = performOperation(num1,num2,op)

	base3 = raw_input("Enter Output base: ")
	if not base2.isdigit():
		print "Invalid Base"
		exit()

	if int(base3) != 10:
		result = baseConverter(10,int(base3),str(result),bases)

	print result

if __name__ == '__main__':
	main()