# Here comes elif :-)
people = 30
cars = 40
buses = 15
if cars > people and #people < buses:
	print "We should take the cars"
	
elif cars < people:
	print "We should not take the cars"
	
else:
	print "We can't decide.."
	
if buses > cars:
	print "there are too many buses.."
	
elif buses < cars:
	print "May be we could take the buses."
	
else:
	print "We still can't decide.."
	
if people > buses:
	print "Alright, let's just take the buses."
	
else:
	print "Fine, let's stay home then."	