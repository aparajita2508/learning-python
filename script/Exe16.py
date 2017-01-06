from sys import argv
script, filename = argv
print "We are going to erase %r" %filename
print "If you don't want that then hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "opening the file"
target = open(filename, 'w')
print "Truncating the file. 'GOODBYE'"
target.truncate()
print "Now I am going to ask you for three lines."
line1 = raw_input("Line1 : ")
line2 = raw_input("Line2 : ")
line3 = raw_input("Line3 : ")
print "I am going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally we close it..."
target.close()
