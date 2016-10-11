## DICTIONARIES ##
# create a dictionary
book = {"title":"Nudge","author":"Thaler and Sunstein","year": 2008}

#accessing an element
print book["title"]
titlestr = "year"
yr = book[titlestr]
print yr

# index by keys, not numbers
# the following would give an error
# print book[0] 

# beware of undefined keys
# print book["publisher"]
# would give an error unless publisher had been defined

# changing the value of an existing key
book["title"] = "new title"
print book["title"]

# create a new key value pair
pub = "publisher"
book[pub] = "Penguin"
print book[pub]

# incrementing a value
book["year"] = book["year"] + 1
print book["year"]

# checking if a key is defined
if "sales" in book:
    print "sales count is filled in"
else:
    print "please track down sales for this book"

if "title" in book:
    print "title is filled in"
else:
    print "please track down title for this book"

# alternative syntax!
if book.has_key("title"):
    print "title is filled in"
else:
    print "please track down the title for this book"

# getting a list of keys
mykeys = book.keys()
print type(mykeys)
print len(mykeys)
print mykeys

# removing a key value pair
print "keys are", book.keys()
print "and the values are", book.values()
del book['title']
print "after deleting, keys are", book.keys()
print "and the values are", book.values()

# alternatively, you can "pop" a value to use
# first, i'll put it back in:
book['title'] = "Nudge"

# new format
print "keys are", book.keys()
print "and the values are", book.values()
title = book.pop("title")
print "after popping, keys are", book.keys()
print "and the values are", book.values()
print "the popped title is", title

# removing all key-value pairs
book.clear()
print "after clear, keys are", book.keys()
print "and values are", book.values()

## word frequency ##
s = "meet cat meet bat cat sat on mat bat sat on cat"
words = s.split()
# create an empty dictionary
d = {}
for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print d


# .get(key, default_value) method
d = {}
d["mat"] = 3
print "mat" in d
print "sat" in d
print d.get("mat", 150)
print d.get("sat", 150)

s = "meet cat meet bat cat sat on mat bat sat on cat"
# a simpler version 
                        
words =s.split()
d = {}
for word in words:
    d[word] = d.get(word,0)+1
print d

# looping through a dictionary's keys
# and printing values
ks = d.keys()
print ks
for k in ks:
    print d[k]

