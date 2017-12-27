# Python Program to find the factors of a number

def print_factors(n):
	print 'Factors of {0} are:'.format(n)
	for x in xrange(1,n+1):
		if n % x == 0:
			print x

n1 = int(input('Enter a n1: '))
print_factors(n1)