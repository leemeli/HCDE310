myglobal = 0

def print_myglobal():
    print "in print_myglobal():", myglobal

def actually_increase_myglobal_byone():
    global myglobal
    myglobal = myglobal+1


def increase_myglobal_byone():
    myglobal = myglobal+1
    print "in increase_myglobal_byone():", myglobal


print "at the start: ", myglobal
print_myglobal()
## so we can get the value of a global
## without declaring it

actually_increase_myglobal_byone()
print "after actually_increase_myglobal_byone():", myglobal
## actually_increase_myglobal_byone() actually
## increases it by one, as advertised
## because we declared it as a global

print_myglobal()

increase_myglobal_byone()
print "after increase_myglobal_byone():", myglobal
## if we don't declare it, but try to modify it
## we get an error back. so you can access globals w/o
## being explicit that they are global, but you can't 
## change them otherwise


