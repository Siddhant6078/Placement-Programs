# Program to check Armstrong numbers in certain interval

lower = int(input('Enter lower: '))
upper = int(input('Enter upper: '))

for num in xrange(lower,upper+1):
	order = len(str(num))
	sum = 0

	temp = num
	while temp > 0:
		r = temp % 10
		sum += r ** order
		temp /= 10

	if sum == num:
		print '{0} is Armstrong Number'.format(num)