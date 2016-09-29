# methods & split
print "HCDE310 is a (tbd) class".split()

print "The  quick brown     fox".split()
print "Human Centered Design & Eng, UW ".split(",")

# multiple ways to apply operations
x = 3
y = 4
# e.g, operators
print x + y     
# e.g., functions
from operator import add
print add(x,y)
# e.g., methods
print x.__add__(y)

# mutability: difference between lists and strings
y = [1, 2, 3]
y[0] = 'a'
print y

x = '123'
x[0] = 'a'
print x

# list modification
# deletion
A = ['a', 'b', 'c', 'd', 'e']
del A[0]
print A
del A[0:2]
print A
# insertion
A = ['b', 'c']
A.insert(0, 'a')
print A
A.append('d')
print A
A.extend(['e', 'f'])
print A
