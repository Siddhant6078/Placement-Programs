# Python program to find the H.C.F of two input number

def computeHCF(n1,n2):
	if n1 < n2:
		smaller = n1
	else:
		smaller = n2
	for x in xrange(1,smaller+1):
		if (n1 % x == 0) and (n2 % x == 0):
			hcf = x
	return hcf

n1 = int(input('Enter a n1: '))
n2 = int(input('Enter a n2: '))

print 'HCF of {0} and {1} is {2}'.format(n1,n2,computeHCF(n1,n2))