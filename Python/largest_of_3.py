# Find the Largest Among Three Numbers

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a > b and a > c:
	print '{0} is Largest'.format(a)
elif b > a and b > c:
	print '{0} is Largest'.format(b)
else:
	print '{0} is Largest'.format(c)