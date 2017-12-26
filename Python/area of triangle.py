# Python Program to find the area of triangle

a = float(input('Enter value of a: '))
b = float(input('Enter value of b: '))
c = float(input('Enter value of c: '))

s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

print 'The area of triangle is %0.2f'%area