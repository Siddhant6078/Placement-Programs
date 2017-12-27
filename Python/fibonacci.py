# Fibonacci sequence up to n-th term where n is provided by the user

num = int(input('Enter num: '))

f0 = 0
f1 = 1
count = 0

if num < 0:
	print 'Please enter positive number'
elif num == 0:
	print f0
elif num == 1:
	print f0
	print f1
else:
	print f0
	print f1
	while count < (num-2):
		f2 = f0 + f1
		print f2
		f0 = f1
		f1 = f2
		count += 1 