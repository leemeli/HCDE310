
## no side effects
def no_side_effect(x,y):
    x = y
    print "x, y =", x, y

a = 3
b = 4
print "a, b =", a, b, "before call"
no_side_effect(a, b)
print "a, b =", a, b, "after call" 

x = 3
y = 4
print "x, y =", x, y, "before call"
no_side_effect(a, b)
print "x, y =", x, y, "after call"


## global variables :-(
def noargs():
    global x
    x = x+3

x = 0
noargs = ()
print x

## assigning variable based on return values
def incr3(y):
    return y+3

x = 0
x = incr3(x)
print x

## mutable objects as parameters
def changeit(mylist):
    mylist[0] = "UW"
    mylist[1] = "Huskies"
    mylist[2] = "are undefeated"
    
classlist = ['310','students','are great']
changeit(classlist)
print classlist

x = [3,4]
y = [4,5]
print "x, y =", x, y, "before call"
no_side_effect(x, y)
print "x, y =", x, y, "after call" 

## default parameters
# motivation: iterating n times
for i in range(4):
    print "i = ", i

for i in range(1,10,2):
    print "i =", i

## default parameters
initial = 7
def f(x, y = 3, z = initial):
    print "x, y, z are", x, y, z

f(2)
f(2,5)
f(2,5,8)

#some omission
f(2, y=5)
f(2, z=10)

#default evaluated at def time
initial = 0
f(2)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's",state,"!"

parrot(action="VOOOOOOM",voltage=1000000)

## nested lists, dictionaries, and other objects
nested1 = [['a','b','c'],['d','e'],['f','g','h']]
nested2 = [1, 'hi', ['a','b','c'], ['d','e'],['f','g','h']]
nested3 = {'k1':[1,2,3],'k2':{'subk1':4}}

print '----nested1----'
print len(nested1)
for x in nested1:
    print type(x)
    print len(x)
    print x[0]

print "\n"
print '----nested2----'
nested2 = [1,'hi',['a','b','c'],['d','e'],['f','g','h']]
print len(nested2)
for x in nested2:
    print type(x)
    if type(x)=='list':
        print len(x)
        print x[0]
    else:
        print x

print "\n"
print '----nested ieration----'
nested1 = [['a','b','c'],['d','e'],['f','g','h']]
for x in nested1:
    print "level1: "
    for y in x:
        print "\tlevel2: " + y


### two quick things ###
print "\n--- two quick things ---"
### Returns
# you can only return once.
def testReturn():
    for i in range(5):
        print i
        return i+10
        
print testReturn()

# but you can include multiple returns
def testReturn2(n):
    if n>5:
        return "more than 5"
    elif n<5:
        return "less than 5"
    return "it is 5"
    
print testReturn2(1)
print testReturn2(5)
print testReturn2(10)