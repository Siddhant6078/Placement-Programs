# Python Program to display the powers of 2 using anonymous function

num = int(input('How many terms: '))

result = list(map(lambda x:2**x,range(num)))

print 'Total terms is {0}'.format(num)

for x in xrange(num):
	print '2 raised to power {0} is: {1}'.format(x,result[x])