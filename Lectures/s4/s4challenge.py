f = open("sherlock.txt",'r')
fstring = f.read()    #assign fstring long string with the whole file


# This is a function that will replace (most) punctuation
# you'll see it again in the homework
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!-;*/")

wordlist = fstring.split()

### Challenge 0: count the number of times the words
### elementary and obviously appear in Sherlock Holmes
### note that we have already opened, read, and split the
### file for you above

### fill in your code here
elementary = 0
obviously = 0

for word in wordlist:
    current = word.lower()
    current = stripWordPunctuation(current)
    if current == "elementary":
        elementary = elementary + 1
    elif current == "obviously":
        obviously = obviously + 1
print "elementary", elementary
print "obviously", obviously



### Challenge 1: modify the code below to print
### all of the words that appear more than 10 times
### and the number of times they appear
###
d = {}
for word in wordlist:
    current = word.lower()
    current = stripWordPunctuation(current)
    d[word] = d.get(word,0)+1
for dictWord in d:
    if d[dictWord] > 10:
        print dictWord, d[dictWord]


###
### Challenge 2: modify and add to your code
### to print the word that appears the most.
### Extra challenge 1: make all words lower case first.
### Extra challenge 2: remove punctuation using 
###                    stripWordPunctuation()

#freqs = {}            #an empty dictionary to keep track of frequency
# tally

largest = 0
mystring = ""
d = {}
for word in wordlist:
    current = word.lower()
    current = stripWordPunctuation(current)
    d[word] = d.get(word,0)+1
for dictWord in d:
    if d[dictWord] > largest:
        largest = d[dictWord]
        mystring = dictWord
print dictWord, largest

# print tally
# printing only words appearing more than 10 times