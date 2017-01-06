def cheese_and_crackers(cheese_count, boxes_of_crackers):

	print "You have number of cheese %d!" %cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for party!"
	print "Get a blanket\n"
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(30, 50)
	
	
print "OR, we can use variables from ours script:"
	
amount_of_cheese = 20
amount_of_crackers = 40
	
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
	
print "We can even do maths inside too:"
	
cheese_and_crackers(10+5, 5+11)
	
print "And we can combine the two, variables and math:"
	
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+50)