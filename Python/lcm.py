# Python Program to find the L.C.M. of two input number

def computeLCM(a,b):
	if a > b:
		greater = a
	else:
		greater = b

	while(True):
		if (greater % a == 0) and (greater % b == 0):
			lcm = greater
			break
		greater += 1
	return lcm

n1 = int(input('Enter a n1: '))
n2 = int(input('Enter a n2: '))

print 'LCM of {0} and {1} is {2}'.format(n1,n2,computeLCM(n1,n2))