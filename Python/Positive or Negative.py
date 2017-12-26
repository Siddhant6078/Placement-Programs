# Program to Check if a Number is Positive, Negative or 0

# Using if...elif...else

num = float(input('Enter a Number: '))

if num > 0:
	print 'Positive'
elif num == 0:
	print 'Zero'
else:
	print 'Negative'

# Using Nested if

if num >= 0:
	if num == 0:
		print 'Zero'
	else:
		print 'Positive'
else:
	print 'Negative'