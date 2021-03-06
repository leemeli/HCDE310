
### you will need this function later in the homework
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;*:[]-+/&")

print "== part 3 =="
### part 3: fieldType() function
# In hw3feed.txt, note that there are both posts and comments in this feed. There are also posters.
# These lines each start with post:, comment:, and from: respectively.
# You are probably thinking "it would be really helpful if we had a function that I could
# use to figure out which type of content a line contains."
#
# The good news is that now you will write that function. 
#
# We have included some starter code to define a function fieldType(). This function should take a line as
# parameter and return the field type (either post, comment, or from).

def fieldType(line):
    firstCharacters = line[:8]
    if firstCharacters.find("post") > -1:
        return "post"
    elif firstCharacters.find("comment") > -1:
        return "comment"
    else:
        return "from"

# You can uncomment and test your function with these lines
print fieldType("from: Sean")
print fieldType("post: Hi everyone")
print fieldType("comment: Thanks!")

print "== part 4 =="
# Find out and print how many posts there are
# as well as how many comments there are
# 
# Print them as:
# Total posts: <number>
# Total comments: <number>
#

posts = 0
comments = 0

fname = "hw3feed.txt"
f = open(fname,'r')

# Fill in your code here.

for line in f:
    currentType = fieldType(line)
    if currentType == "post":
        posts = posts + 1
    elif currentType == "comment":
        comments = comments + 1

print "Total posts: %d"%posts
print "Total comments: %d"%comments

print "== part 5 =="
### part 5: printing users

# Your job is to extract the names form the post: lines and print them out,
# exactly as it is shown in the screenshot in the PDF file. Hint: if you 
# want to remove "from:" you can use string slicing operations or the replace method.

# You may use the fieldType() function but you do not have to. You may also define
# another function, such as fieldContents(), to help you but that optional. 

# Duplicate names are expected for this part!

fname = "hw3feed.txt"
f = open(fname,'r')
#fill in code here
for line in f:
    if fieldType(line) == "from":
        print line[6:]


print "== part 6 =="
### part 6: counting poster contribution frequency
# See the instructions in the PDF file. They are easier to follow with
# formatting

pc_count = {}
f = open(fname,'r')

# read in and count the total number of posts and comments for each user

#fill in code here
for line in f:
    currentType = fieldType(line)
    currentName = ""
    if currentType == "from": 
        currentName = line[6:-1]
        pc_count[currentName] = pc_count.get(currentName, 0) + 1


# print the number of times each user posted

#fill in code here
keys = pc_count.keys()
for dictElement in keys:
    print dictElement + ": " + str(pc_count[dictElement])
    

# part 6 - Just for fun: how many unique posters were there?
# (note this question is optional - but it's one line of code)

print "== part 7 =="
### part 7: counting word frequency
# This is similar to post count in part 6 and you might
# even re-use some of your code. Count the number of
# times each word appears in all posts, but *not* comments
#
# use the stripWordPunctuation() function to get rid of punctuation.
# note that it is not perfect so some extra punctuation may remain.
#
# you should also convert all words to lowercase when counting.
# I.e., "the" and "The" should be the same word

postWordCount = {}
f = open(fname,'r')

# read in and count of times each word appeared

#fill in code here
for line in f:
    currentType = fieldType(line)
    if currentType == "post": 
        currentPost = line[6:-1]
        wordList = currentPost.split()
        for word in wordList:
            currentWord = stripWordPunctuation(word)
            currentWord = currentWord.lower()
            postWordCount[currentWord] = postWordCount.get(currentWord, 0) + 1
        

# print the number of times each word appeared

#fill in code here
keys = postWordCount.keys()
for dictElement in keys:
    print dictElement + ": " + str(postWordCount[dictElement])

print "== part 8 =="
### part 8: counting word frequency in comments and posts
# for this part, write a function, wordFreq() that will return
# the word frequency in either posts or comments as a dictionary

# This function must must take a file name and the field type
# (either post or comment) as parameters

# For example, if I want to get a dictionary of word counts in
# the posts in hw3feed.txt, I should be able to call:
# wordFreq('hw3feed.txt','post')

# You can use your code from part 7 as a starting point, or
# if you wrote part 7 using a function, you may simply edit it
# to meet the requirements for this part.

# uncomment and begin editing from the next line:
def wordFreq(fname, commentOrPost):
    postWordCount = {}
    f = open(fname,'r')
    for line in f:
        currentType = fieldType(line)
        if currentType == commentOrPost: 
            currentPost = line[6:-1]
            wordList = currentPost.split()
            for word in wordList:
                currentWord = stripWordPunctuation(word)
                currentWord = currentWord.lower()
                postWordCount[currentWord] = postWordCount.get(currentWord, 0) + 1
    return postWordCount

# to test ,you can uncomment and run these  lines:
if wordFreq(fname,'post')["anyone"] == 9 and wordFreq(fname,'post')["eclipse"] == 5:
    print "Looks like wordFreq() works fine for posts"
else:
    print "We got some errors with wordFreq() for posts."
  
if wordFreq(fname,'comment')["file"] == 24 and wordFreq(fname,'comment')["if"] == 39:
    print "Looks like wordFreq() works fine for comments"
else:
    print "We got some errors with wordFreq() for comments."

