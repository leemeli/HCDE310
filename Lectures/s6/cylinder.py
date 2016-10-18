#class Cylinder():
#    """A cylinder."""
#    def __init__(self,height,radius):
#        self.height = height
#        self.radius = radius
#mycylinder = Cylinder(10,2)       

import math      
class Cylinder():
    """A cylinder."""
    def __init__(self,height,radius,thickness=None):
        self.height = height
        self.radius = radius
        self.thickness = thickness
        if thickness == None: 
            self.capacity = 0
        else:
            innerradius = self.radius - self.thickness
            self.capacity = math.pi * innerradius**2 * self.height
        self.contents = 0
    def addLiquid(self,amount):
        self.contents += amount
        if self.contents > self.capacity:
            print "uh oh I overflowed."
            self.contents = self.capacity
    def removeLiquid(self,amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            print "sorry, you were %0.2f short."%abs(self.contents)
            self.contents = 0


mycylinder = Cylinder(10,2)
mug = Cylinder(3.75,1.62,.12)
cup = Cylinder(6,1.5,.05)
barrel = Cylinder(35,12,0.06)

totalcapacity = 0
for cyl in [mycylinder,mug,cup,barrel]:
    totalcapacity += cyl.capacity
print totalcapacity

mug.addLiquid(10)
print "Current contents: %0.2f, capacity: %0.2f"%(mug.contents, mug.capacity)
mug.addLiquid(25)
print "Current contents: %0.2f, capacity: %0.2f"%(mug.contents, mug.capacity)
mug.removeLiquid(5)
print "Current contents: %0.2f, capacity: %0.2f"%(mug.contents, mug.capacity)
mug.removeLiquid(30)
print "Current contents: %0.2f, capacity: %0.2f"%(mug.contents, mug.capacity)