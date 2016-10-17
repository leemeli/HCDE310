### a simple function
def hello():
    print "Hello"
    print "Glad to meet you"

hello()
print "Done with the first call"
hello()

### parameter passing
def hello2(s):
    print "Hello " + s

hello2("class")
hello()        
hello2("world")

# but hello2() would give an error
# since hello2 expects a parameter


### an example comparison function

def comp(x,y):
    print "x = "+str(x)
    print "y = "+str(y)
    if (x>y):
        print "x is bigger"
    elif (x<y):
        print "y is bigger"
    else:
        print "They're the same"

z = 4
comp(2,5)
comp(5,z)
comp(z,4)

### CYU2

def CYU2(s1, s2):
    x = len(s1)
    y = len(s2)
    if x > y:
        print s1
    else:
        print s2

CYU2("Hello","goodbye")
CYU2("love","hate")

### functions with return values

def square(x):
    return x*x

y = 2
print square(3)
print square(3) + y
print square(3+y) 
y = square(y)
print y
print square(square(2))

# cyu 3

def CYU3(s1, s2):
    x = len(s1)
    y = len(s2)
    return y - x

z = CYU3("Yes", "no")
if z > 0:
    print "the first one was longer"
elif z == 0: 
    print "they are the same length"
else:
    print "the second one was longer"

### order of evaluation
# remember that we already have square() defined above

def g(y):
    return y + 3

print square(g(2))

### functions that call functions
# remember that we already have square() defined above

def square(x): 
    return x*x

def h(y):
    return square(y) + 3

print h(2)
print g(h(2))

### stack variables
def local_function():
    x = "new string"

def main():
    x = "old string"
    local_function()
    print x

main()


## cyu -- scope test

def f1(something):
    print "in function f1: ", something

def f2(something):
    print "in function f2: ", something
    print fred

def scope_test():
    fred = "Mr. Rogers"
    answer = 42
    f1(answer)
    f2(answer)

scope_test()
