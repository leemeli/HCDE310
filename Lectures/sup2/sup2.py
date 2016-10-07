# review exercise
# this prints the first word from each line
# change it to print the last one instead
fh = open('test.txt','r')
for xh in fh:
    w = xh.split()
    print w[0]
    
# types
print type(2+3)
print type(2+3.0)
print type('hello'+'there')
print type('hello there'.split())

# concatenating string and number
for i in [1,2,3]:
    print "user" + str(i) + ", you are a winner"
    
#experiments
print 4/3
print float(4)/3
x=4
y=3
print float(x)/float(y)
print int(157.23*100)
print str(4)+str(3)
print int(4.7)
print int(-4.7)
#print int("hello")

#dollars to cents
#you'll have to comment out any of the above lines
#that give errors before you can run this
dollars = 157.23
print 100*dollars
print int(100*dollars)
print round(100*dollars)
print int(round(100*dollars))

#octals
zipcode = 024132
print zip

#this next line will give an error, since 9
#does not make sense in octals
zip = 02492

#splitting 
fromline = "From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
print len(fromline.split())
print fromline.split(" ")
print len(fromline.split(" "))
print fromline.split(",")
