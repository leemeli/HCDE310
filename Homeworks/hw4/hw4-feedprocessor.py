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


# the following code runs your functions to make sure they work properly
# uncomment all valid lines of python code to test your functions

# read in and count contributions
#contributions = contributorCounts("hw4feed.txt")

# print the human readable version
#print '------'
#printContributors(contributions)

# write the computer readable version
#saveContributors(contributions, 'contribs.csv')


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
#def wordFreqs(fname):


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
#def writeFreqs(freqdict):

# finally, uncomment these two lines to test your functions    
#fd = wordFreqs('hw4feed.txt')
#writeFreqs(fd)
