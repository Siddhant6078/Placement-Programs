# Python program to display all the prime numbers within an interval

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print 'Print prime numbers between {0} and {1} are: '.format(lower,upper)

for num in xrange(lower,upper+1):
	if num > 1:
		for n in range(2,num):
			if num % n ==0:
				break
		else:
			print '{0}'.format(num)