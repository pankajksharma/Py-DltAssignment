import os

def baseConverter(ibase,obase,inum,bases):
	negNum = 0
	if inum.find('-') == 0:
		negNum = 1
	
	for n in list(inum):
		if not bases.has_key(n) or bases[n] >= ibase:
			if n != '.' and n != '-':
				print bases[n],n
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
			onum.append(bases[fr])
			fracSum = fracSum - fr
			if fracSum == 0.0:
				break
			count = count + 1			

	return (''.join(onum))

def fill(frac,len1,len2):
	frac = list(frac)
	for i in range(len1-len2):
		frac.append('0')
	return ''.join(frac)

def doOr(frac1,frac2):
	orres = []
	for i in range(0,len(frac1)):
		if frac1[i] == '0' and frac2[i] == '0':
			orres.append('0')
		else:
			orres.append('1')
	out = ''.join(orres)
	return out

def doAnd(frac1,frac2):
	andres = []
	for i in range(len(frac1)):
		if frac1[i] == '1' and frac2[i] == '1':
			andres.append('1')
		else:
			andres.append('0')
	return ''.join(andres)

def performOperation(num1,num2,op,bases):
	if op == '+':
		return num1 + num2
	elif op == '-':
		return num1 - num2

	elif op == '/':
		return num1/num2

	elif op == '*':
		return num1*num2
	
	elif op == '|':
		frac1 = '0.'+str(num1).split('.')[1]
		frac2 = '0.'+str(num2).split('.')[1]
		#print frac1,frac2
		if frac1 != '0.0':
			frac1 = float('0.'+baseConverter(10,2,frac1,bases).split('.')[1])
		else:
			frac1 = float(frac1)
		if frac2 != '0.0':
			frac2 = float('0.'+baseConverter(10,2,frac2,bases).split('.')[1])
		else:
			frac2 = float(frac2)
		frac1 = str(frac1).split('.')[1]
		frac2 = str(frac2).split('.')[1]
		if len(frac1)<len(frac2):
			frac1 = fill(frac1,len(frac2),len(frac1))
		elif len(frac2)<len(frac1):
			frac2 = fill(frac2,len(frac1),len(frac2))
		#print frac1,frac2
		facOr = '0.'+doOr(frac1,frac2)
		facOr = baseConverter(2,10,facOr,bases)
		return str(int(num1) | int(num2))+facOr


	elif op == '&':
		frac1 = '0.'+str(num1).split('.')[1]
		frac2 = '0.'+str(num2).split('.')[1]
		#print frac1,frac2
		if frac1 != '0.0':
			frac1 = float('0.'+baseConverter(10,2,frac1,bases).split('.')[1])
		else:
			frac1 = float(frac1)
		if frac2 != '0.0':
			frac2 = float('0.'+baseConverter(10,2,frac2,bases).split('.')[1])
		else:
			frac2 = float(frac2)
		frac1 = str(frac1).split('.')[1]
		frac2 = str(frac2).split('.')[1]
		if len(frac1)<len(frac2):
			frac1 = fill(frac1,len(frac2),len(frac1))
		elif len(frac2)<len(frac1):
			frac2 = fill(frac2,len(frac1),len(frac2))

		facAnd = '0.'+doAnd(frac1,frac2)
		facAnd = baseConverter(2,10,facAnd,bases)
		return str(int(num1) & int(num2))+facAnd

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
	base1 = raw_input("\nEnter Base 1: ")
	if not base1.isdigit() or (int(base1) > 62 or int(base1) < 2):
		print "Invalid Base"
		exit()
	num1 = raw_input("Enter first number (in base %s): "%base1)
	num1 = float(baseConverter(int(base1),10,num1,bases))
	#print num1

	ch=raw_input("\nMenu:\n1->Base Conversion\n2->Logical Not\n3->Anything Else\nEnter Choice: ")

	if int(ch)==1 or int(ch)==2:
		base3 = raw_input("\n\nEnter Output base: ")
		if not base3.isdigit() or (int(base3) > 62 or int(base3) < 2):
			print "Invalid Base"
			exit()
	if int(ch)==1:
		result = baseConverter(10,int(base3),str(num1),bases)
		print 'Output:',result
		exit()

	if int(ch)==2:
		result=list(baseConverter(10,2,str(num1),bases))
		print result
		for i in range(len(result)):
			if result[i]=='1':
				result[i]='0'
			elif result[i]=='0':
				result[i]='1'
		out=''.join(result)
		print result
		result = baseConverter(2,int(base3),out,bases)
		print 'Output:',result
		exit()

	base2 = raw_input("\n\nEnter Base 2: ")
	if not base2.isdigit() or (int(base1) > 62 or int(base1) < 2):
		print "Invalid Base"
		exit()
	num2 = raw_input("Enter second number (in base %s): "%base2)
	num2 = float(baseConverter(int(base2),10,num2,bases))
	#print num2

	validOp = ['+','-','&','|','/','*']
	op = raw_input('\n\nValid Operations: \n(+ -> Add  - -> "Subtract(1-2)"  & -> "Logical And"  | -> "Logical Or"  / -> Divide(1/2) * -> Multiply)\n\nEnter a symbol: ')
	if op not in validOp:
		print 'Invlid Operand'
		exit()

	result = performOperation(num1,num2,op,bases)

	base3 = raw_input("\n\nEnter Output base: ")
	if not base3.isdigit() or (int(base3) > 62 or int(base3) < 2):
		print "Invalid Base"
		exit()

	if int(base3) != 10:
		result = baseConverter(10,int(base3),str(result),bases)

	print 'Output:',result

	print '\nValues for Conversion:'
	print str(sorted(bases.items(), key=lambda x: x[1])).replace('[','').replace(']',''),'\n\n'

if __name__ == '__main__':
	main()
