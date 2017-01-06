def add(a, b):
	print "adding %d+%d" %(a,b)
	return a+b
	
def subtract(a,b):
	print"Subtracting %d -%d" %(a,b)
	return a-b
	
def multiply(a,b):
	print "Multiplying %d*%d" %(a,b)
	return a*b
	
def divide(a,b):
	print"Dividing %d/%d" %(a,b)
	return a/b
	
	print "Let's do some maths with functions:\n"
	
age = add(30, 5)
height = subtract(150, 5)
weight = multiply(12, 5)
iq = divide(100,2)
print "Age %d, Height %d, Weight %d, iq %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what print "Can you do it by hand?"