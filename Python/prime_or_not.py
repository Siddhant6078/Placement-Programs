# Python program to check if the input number is prime or not

num = int(input('Enter num: '))

if num > 1:
	for n in range(2,num):
		if num % n ==0:
			print '{0} is not Prime'.format(num)
			break
	else:
		print '{0} is Prime'.format(num)