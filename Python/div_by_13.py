# Find numbers divisible by thirteen from a list using anonymous function

my_list = [12, 65, 54, 39, 102, 339, 221]

result = list(filter(lambda x: (x % 13 == 0),my_list))

print 'Numbers divisible by 13 are: ',result