######################################
# part 2: contributor counts

#Your next task is to extend the functionality from last week's homework
#assignment using functions. In the last assignment, you read in the contents
#of a file, computed the poster contribution frequencies using a dictionary, and
#printed out the contents of that dictionary.

#This week, you'll write a function that computes the poster frequencies and
#returns the dictionary as a value. The dictionary will then be passed as a
#parameter to two more functions that will do something with it.
#
#Note that we will still be working with the hw#feed.txt (hw4feed.txt) format. 
#Next week, we'll start using JSON in the larger parts of the assignment.
#

#### isField() tests if the line represents the given kind of field
# you don't have to modify this function.
# inputs:
#   field_name: a string that specifies the kind of field
#   s: the string we are testing
# returns: True if s starts with field, False otherwise
def isField(field_name, s):
    if s[:len(field_name)] == field_name:
        return True
    else:
        return False

#### contributorCounts() should return post and comment frequency for each user
# in the specified file
# input:
#   file_name: name of file being read
# returns: a dictionary of post and comment counts
# e.g., if we we had two posters, Alice (0 comments, 2 posts) and Bob (1 post, 2 comments), 
# our dictionary would look like
# cc = {"Alice":{"posts":2,"comments":0},"Bob":{"posts":1,"comments":2}}

# define contributorCounts() here.
# in this function, you MUST make at least one call to the function isField
# or another function you have defined
def contributorCounts(file_name):
    f = open(file_name,'r')
    dict = {}
    currentUser = ""
    currentType = ""
    for line in f:
        if isField("from", line):
            currentUser = line[6:-1]
        elif isField("post", line):
            currentType = "posts"
            dict[currentUser] = dict.get(currentUser, {})
            dict[currentUser][currentType] = dict[currentUser].get(currentType, 0) + 1
        elif isField("comment", line):
            currentType = "comments"
            dict[currentUser] = dict.get(currentUser, {})
            dict[currentUser][currentType] = dict[currentUser].get(currentType, 0) + 1
    return dict

#My test to make sure it works
#fname = "hw4feed.txt"
#f = open(fname,'r')
#print contributorCounts(f)



#### printContributors() should print out the number of times each
# person posted and commented.
# The implementation should be similar to what was done in hw3 to print out
# contributor counts, but will use an if statement so that contributor counts of
# 1 will be printed as "once" and higher or zero counts will be "X times". For
# example:
#   "John Smith posted once and commented 2 times"
#   "Jane Smythe posted 4 times and commented 0 times"
#
# input parameter:
#   counts: dictionary of contributor counts

# define printContributors() here.
def printContributors(counts):
    for person in counts:
        myString = person + " posted "
        currentPerson = counts[person]
        if currentPerson.has_key("posts") == False: #If the person never posted
            myString = myString + "0 times and commented "
            if currentPerson["comments"] == 1:
                myString = myString + "once"
            else:
                myString = myString + str(currentPerson["comments"]) + " times"
        elif currentPerson.has_key("comments") == False: #If the person never commented
            if currentPerson["posts"] == 1:
                myString = myString + "once"
            else:
                myString = myString + str(currentPerson["posts"]) + " times"
            myString = myString + " and commented 0 times"
        else: #If the person has posted and commented
            if currentPerson["posts"] == 1:
                myString = myString + "once"
            else:
                myString = myString + str(currentPerson["posts"]) + " times"
            myString = myString + " and commented "
            if currentPerson["comments"] == 1:
                myString = myString + "once"
            else:
                myString = myString + str(currentPerson["comments"]) + " times"
        print myString

#My test to make sure it works
#fname = "hw4feed.txt"
#f = open(fname,'r')
#printContributors(contributorCounts(f))

#### saveContributors() should save a comma separated value (CSV) formatted
# file where the first item is the key of a dictionary and the second item is
# the value (e.g. name,postcount,commentcount).
# input parameters:
#   counts: dictionary of contributor counts
#   output_fname: name of the file being saved to

# the first line in the file should be a header row, that is, a row that just
# contains the following text describing the data:
# name,postcount,commentcount 

# define saveContributors() here.
def saveContributors(counts, output_fname):
    f=open(output_fname, 'w')
    f.write("name, postcount, commentcount \n")
    for person in counts:
        currentRow = person + ","
        currentDict = counts[person]
        if currentDict.has_key("posts") and currentDict['posts'] > 0:
            currentRow = currentRow + str(currentDict['posts'])
        else:
            currentRow = currentRow + '0'
        currentRow = currentRow + ","
        if currentDict.has_key("comments") and currentDict['comments'] > 0:
            currentRow = currentRow + str(currentDict['comments'])
        else:
            currentRow = currentRow + '0'
        f.write(currentRow + "\n")
    f.close

# the following code runs your functions to make sure they work properly
# uncomment all valid lines of python code to test your functions

# read in and count contributions
#fname = "hw4feed.txt"
#f = open(fname,'r')
contributions = contributorCounts("hw4feed.txt")

# print the human readable version
print '------'
printContributors(contributions)

# write the computer readable version
saveContributors(contributions, 'contribs.csv')


######################################
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;*:[]-+/")


######################################
# part 3: word counts

# To do this, we will write two functions. The first wordFreqs() which
# should take a file name as a parameter and generate a dictionary of
# words and their frequencies in posts and comments. 
#
# That is, the output should be a dictionary in the form:
# {'word':{'comments':3,'posts':5},'anotherword':{'comments':0,'posts':5}
# .... and so on. That is, it's another nested dictionary. 
#
# uncomment the next line and define wordFreqs() there
def checkStopWords(wordToCheck):
    f = open('stopwords.txt', 'r')
    currentBoolean = True #word okay to use
    for word in f:
        word = word.strip()
        word = stripWordPunctuation(word).lower()
        wordToCheck = stripWordPunctuation(wordToCheck).lower()
        if word == wordToCheck:
            currentBoolean = False #Word not okay to use
    return currentBoolean

def wordFreqs(fname):
    f = open(fname,'r')
    dict = {}
    for line in f:
        if isField("comment", line):
            currentString = line[8:-1]
            currentWords = currentString.split(" ")
            for word in currentWords:
                if checkStopWords(word) == True:
                    word = stripWordPunctuation(word)
                    dict[word] = dict.get(word, {})
                    dict[word]["comments"] = dict[word].get("comments", 0) + 1
        if isField("post", line):
            currentString = line[5:-1]
            currentWords = currentString.split(" ")
            for word in currentWords:
                if checkStopWords(word) == True:
                    word = stripWordPunctuation(word)
                    dict[word] = dict.get(word, {})
                    dict[word]["posts"] = dict[word].get("posts", 0) + 1
    return dict


# Next, we will write your writeFreqs() function, which takes, as a parameter
# a dictionary of the format output by wordFreqs() and writes a CSV file, freqs.csv.
# The first line of your file should be:
# word,postcount,commentcount
# and subsequent lines should contain the data.
#
# You must remove stopwords (the words in stopwords.txt). You may remove
# them in either wordFreqs() or in writeFreqs(). The decision is up to you.
# 
# uncomment the next line and define writeFreqs() there.
def writeFreqs(freqdict):
    f=open('freqs.csv', 'w')
    f.write("word, postcount, commentcount \n")
    for word in freqdict:
        currentRow = word + ","
        currentDict = freqdict[word]
        if currentDict.has_key("posts") and currentDict['posts'] > 0:
            currentRow = currentRow + str(currentDict['posts'])
        else:
            currentRow = currentRow + '0'
        currentRow = currentRow + ","
        if currentDict.has_key("comments") and currentDict['comments'] > 0:
            currentRow = currentRow + str(currentDict['comments'])
        else:
            currentRow = currentRow + '0'
        f.write(currentRow + "\n")
    f.close

# finally, uncomment these two lines to test your functions    
fd = wordFreqs('hw4feed.txt')
writeFreqs(fd)
