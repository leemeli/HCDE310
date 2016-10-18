#importing
import testimport
print testimport.y
print testimport.square(3)

## using localname
import testimport as t
print t.y
print t.square(4)

## importing into local namespace
from testimport import y
print y

### json!
print "\n--- json ---"
import json
post = json.load(open('fbpost.json'))
print post.keys()
print type(post)

print len(post['comments']['data']), "comments"
print type(post['comments']['data'][0])
print post['comments']['data'][0]['message']

comments = post['comments']['data']

for comment in comments:
    print "----next comment----"
    for k in comment.keys():
        print "key is %s; value is %s"%(k,comment[k])
