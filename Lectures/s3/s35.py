
## accumulation pattern, review
# to total....
tot = 0
nums = input("Enter a list of numbers, in square brackets:")
for x in nums:
    tot = tot+x
print tot

## what if we wanted to accumulate to the max?
#nums = input("Enter a list of numbers, in square brackets:")
#max_so_far = #what?
#for x in nums:
#    max_so_far = #what?
#print max_so_far

## boolean type
print 4>3
print type(4>3)
x = 4 == 3
print x
print type(x)

## boolean operators
x = 3
print True and False
print (x==3) and (x<10)
print (x<3) or (x>3)
print (x<3) or (x==3)
print (x<5) or (x==3)
print not(x>5)

## one way conditionals
x = 5
print "Before"
if (x==5):
   print "is 5"
   print "is still 5"
   print "Third 5"
print "after"

faren = 451
if faren > 90:
    print "heat warning"
if faren < 32:
    print "cold warning"
 
