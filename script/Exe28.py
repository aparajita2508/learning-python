"""1. Solve each equality test:
3 != 4 is True
True and not ("testing" != "test" or "Python" =="Python")
"testing" != "test" is True
True and not (True or "Python" == "Python")
"Python" == "Python" 
True and not (True or True)
Find each and/or in parentheses ():
(True or True) is True True and not (True)
Find each not and invert it
not (True) is False: True and False
Find any remaining and/or and solve them 
True and False is False"""

print 3 != 4 and not ("testing" != "test" or "Python" == "Python")
print "test" and "test"
print "False" and "1"
print "True" and "1"
