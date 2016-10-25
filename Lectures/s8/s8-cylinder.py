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
    ## add a string method here
    
    ## add a comparison method here. Have it compare on 
    ## total volume, capacity, contents, or remaining capacity.


mycylinder = Cylinder(10,2)

# let's instead create classses for each of these types of cylinders. 
# for the mug, we might have a handle or set the material, or if it has a lid
# for the cup, we might also define the material
# and the for the oil barrel, we might pick a number of chines

mug = Cylinder(3.75,1.62,.12)
cup = Cylinder(6,1.5,.05)
barrel = Cylinder(35,12,0.06)

