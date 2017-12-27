# Sum of natural numbers up to n where n is provided by user

num = int(input('Enter num: '))
temp = num

if num < 0:
	print 'Please enter positive number'
else:
	sum = 0
	while num > 0:
		sum += num
		num -= 1
	print 'Sum of natural numbers upto {0} is: {1}'.format(temp,sum)