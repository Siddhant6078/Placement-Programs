''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

def add(n1,n2):
	return n1+n2

def sub(n1,n2):
	return n1-n2

def mul(n1,n2):
	return n1*n2

def div(n1,n2):
	return n1/n2

print 'Select Operation:'
print '1. Add'
print '2. Sub'
print '3. Mul'
print '4. Div'

choice = int(input('Enter your choice(1/2/3/4): '))

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

if choice == 1:
	print '{0} + {1} = {2}'.format(n1,n2,add(n1,n2))
elif choice == 2:
	print '{0} - {1} = {2}'.format(n1,n2,sub(n1,n2))
elif choice == 3:
	print '{0} 8 {1} = {2}'.format(n1,n2,mul(n1,n2))
elif choice == 4:
	print '{0} / {1} = {2}'.format(n1,n2,div(n1,n2))
else:
	print 'Invalid Input'