# Python program to check if Armstrong number or not

num = int(input('Enter num: '))

sum = 0

temp = num
while temp > 0:
	r = temp % 10
	sum += r ** 3
	temp /= 10

if sum == num:
	print '{0} is Armstrong Number'.format(num)
else:
	print '{0} is not Armstrong Number'.format(num)