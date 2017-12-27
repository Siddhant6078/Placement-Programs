''' Python program to find the
multiplication table (from 1 to 10)'''

num = int(input('Enter num: '))

for x in xrange(1,10+1):
	print '{0} x {1} = {2}'.format(num,x,num*x)