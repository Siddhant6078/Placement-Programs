# Python program to find the factorial of a number provided by the user.

num = int(input('Enter num: '))

fact = 1

if num < 0:
	print 'Factorial of {0} does not exits'.format(num)
elif num == 0:
	print 'Factorial of {0} is 1'.format(num)
else:
	for x in xrange(1,num+1):
		fact = fact * x
	print 'Factorial of {0} is {1}'.format(num,fact)