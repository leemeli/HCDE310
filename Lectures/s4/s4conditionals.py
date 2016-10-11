# some common problems

# filenames vs. file objects
fname = 'test.txt'
for line in fname:
    print line

# the above will iterate over the characters in the string
# to open the file, we need to use open, like this:
# fname = "test.txt"
# myfile = open(fname)  ## or myfile = open("test.txt")
# for line in myfile:
#     print line

# string names vs variable names
# x = hello
# this would work if we had a variable named hello
# but if we want it as a string, we need to do:
# x = "hello"

# missing identation
for x in [2, 4, 6,]:
    y = x+1
print y

#missing colon

#for x in [2,4,6]
#    print x + 1

## we need a colon after the for line!, e,g:
## for x in [2,4,6]:

# unexpected indent, e.g., 
#print 'hello'
#     print 'hello'

# nothing in for loop
#for x in [2,6,4]:
#print "done"
# the above will get you an error that python expects an indented block
# fyi: if you want a for loop that does nothing, you can do the following:

for x in [2,6,4]:
   pass
print "done"

# attempting to concat a string and integer
#for x in [2,4,6]:
#   print "user" + x
# that will give you an error. instead, try:
#for x in [2,4,6]:
#   print "user" + str(x)
# or 
#for x in [2,4,6]:
#   print "user",str(x)

# forgetting to close a string
# print "sadface

# unbound variables
# misspelled / typos
#hlp = "please help!"
#print hpl
# if you do this, help will not come.

# trying to use them before assigning them
#for x in [2,4,6]:
#    count = count + 1
# ah, but what is count? we need to assign
# it first!

# index out of bounds 
#st = "hello"
#print st[9]
# too far!

# Index at the end of a slice is not inclusive
mystring = "cats"
print mystring[0:3]		# will print "cat"
print mystring [0:4] 		# will print "cats"

### == main part of lecture follows ###

## two way conditionals
x = 7
y = 4
if x<y:
    print "smaller"
else: 
    print "not smaller"
print "done"

x = 2
y = 4
if x < y:
    print "smaller"
else:
    print "not smaller"
print "all done"

## two way cyu
#temp = 4
#if temp-32 > 0:
#   print "warm"
#else:
#   print "cold"

### multiway
t = 40
bp = 212
fp = 32
if t > bp:
   print "gas"
elif t > fp:
    print "liquid"
else:
    print "solid"

### nested conditionals
species = raw_input("Please input a species: ")
if species == 'Dog':
    breed = raw_input("Please type in a dog breed: ")
    if breed == "Collie": 
        name = "Lassie"
    else: 
        name = "Fido"
elif species == 'Cat':
    name = "Fluffy"
elif species == "Velociraptor":
    name= "Clever Girl"
else:
    name = "Whazit"
print "Suggested pet name is", name

## jff: what if we wanted to make the input above case insensitive?

## multuple conditionals
## bad grading:
score = input("Please enter a score (0-100): ")
if score >= 87:
    grade = "A"
if score >= 72:
    grade = "B"
if score >= 67:
    grade = "C"
if score >= 62:
    grade = "D"
else:
    grade = "E"
print grade

## treating nonbooleans as booleans
print bool(0)
print bool(-1)
print bool(32)
print bool("")
print bool(" ")
print bool([])
print bool("\n")
print bool([True])
print bool([False])

ans = raw_input("What flavor do you want [default vanilla]? ")
if ans:
    flavor = ans
else:
    flavor = "vanilla"
print "Your flavor is", flavor

#### boolean inside a for loop
for st in ["bob", "bark at the moon", "where at"]:
    w = st.split()
    if len(w)>2 and w[1] == "at":
        print "++++++++", st
    else:
        print "--------", st
print "done"
