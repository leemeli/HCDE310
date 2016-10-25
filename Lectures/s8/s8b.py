class Dog:
    """A slobbering fiend"""
    
    def __init__(self,n):
        """Initialize with number of woofs"""
        self.woofcount = n
    def bark(self):
        """Bark out loud"""
        for i in range(self.woofcount):
            print "Woof"
    def __str__(self):
        """Called whenever a printed representation of self is needed"""
        return "A dog that barks %d times"%self.woofcount
    def __cmp__(self,other):
        """Return negative number if self < other"""
        return self.woofcount - other.woofcount
        
print "Dog has type", type(Dog)
print "Dog.bark has type", type(Dog.bark)

gromit = Dog(12)
print type(gromit)
print gromit.__class__.__name__
print gromit.__class__ == Dog
print gromit.woofcount

print "\n===gromit.bark()==="
gromit.bark()

Woofus = Dog(1)
print Woofus.woofcount
Woofus.bark()
print "----"
Woofus.woofcount = 2
print Woofus.woofcount
Woofus.bark()


#__cmp___
print "\n __cmp__"
print "Gromit barks less than Woofus?", gromit<Woofus
print "Woofus barks less than Gromit?", Woofus<gromit

