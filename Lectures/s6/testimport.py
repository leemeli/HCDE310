def square(x):
    return x*x
    
y = 10

print "in testimport.py __name__ is %s"%(__name__)
if __name__ == "__main__":
    print square(y)