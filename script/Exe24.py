print "Let's practice everything.\n"
print 'You\'d need to know \'bout escape with \\ that do\n newlines and \t tabs.'
poem = """
\t Ba Ba blacksheep
have you any wool?
\tyes Sir! yes Sirh!
three bags full\n
one for my master\n
one for, my dane
one for the little boy \n\t who lives down a lane
"""
print "---------"
print poem
print "---------------"
five = 10-2+3-6
print "It should be five: %s" %five

def secret_formula(started):
	jelly_beans = started*500
	jars = jelly_beans/1000
	crates = jars/100
	return jelly_beans, jars, crates
	
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
	
print "With the  starting point of: %d" %start_point
print "We'd have %d beans, %d jars, %d crates." %(beans, jars, crates)
	
start_point = start_point / 10
	
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)