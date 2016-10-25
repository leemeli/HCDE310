class Silly:
    """This class does nothing, but we use it to illustrate instances and members"""
    
print "Silly has type ", type(Silly)

# an instance
x1 = Silly()
print "x1 has type ", type(x1)
x1.foo = 3
print x1.foo
print x1.__class__.__name__
print x1.__class__ == Silly

#another instance
x2 = Silly()
x2.foo = 4
print x2.foo
print x1.foo