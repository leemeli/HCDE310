## string output ##
x = 3
y = 3.0
name = "Sean"

print "x is %s"%x
print "x is %d"%x
print "x is %f"%x
print "x is %.2f"%x

print "y is %s"%y
print "y is %d"%y
print "y is %f"%y
print "y is %.2f"%y

print "name is %s"%name
#print "y is %d"%name
#print "y is %f"%name
#print "y is %.2f"%name

print "name is %s, x is %d"%(name, x)

## file output ##
f = open("outputtest-1.txt","w")
f.write("goodbye\n")
f.write("bye now\n")
x = "really. bye"
f.write(x + "\n")
f.close()

## we can write other types ##
f = open("outputtest-2.txt","w")

mylist =['a','b','c']
mydict={"title":"Nudge","author":"Thaler & Sunstein","year":2008}
myint=11
myfloat=7.0

# but have to convert to a string first! 
# otherwise, these will produce errors
f.write(str(mylist))
f.write("\n")
f.write(str(mydict))
f.write("\n")
f.write(str(myint))
f.write("\n")
f.write(str(myfloat))
f.write("\n")

f.close()

## common file output pattern ##
f = open("outputtest-3.txt",'w')
l = ['a','b','c']
for x in l:
    f.write(x)
    # you have to put in your own new lines
    f.write("\n")
f.close()

