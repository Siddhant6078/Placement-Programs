# Python program to swap two variables using 3rd variable

x = input('Enter value of x: ')
y = input('Enter value of y: ')

print 'The value of x: Before:{0}'.format(x)
print 'The value of y: Before:{0}'.format(y)

temp = x
x = y
y = temp

print 'The value of x: After:{0}'.format(x)
print 'The value of y: After:{0}'.format(y)

# Python program to swap two variables without using 3rd variable
a = input('Enter value of a: ')
b = input('Enter value of b: ')

print 'The value of a: Before:{0}'.format(a)
print 'The value of b: Before:{0}'.format(b)

a = a+b
b = a-b
a = a-b

print 'The value of a: After:{0}'.format(a)
print 'The value of b: After:{0}'.format(b)