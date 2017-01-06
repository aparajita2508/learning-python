from sys import argv # we are getting a argument variable from the package sys

script, filename = argv # we are assigning two values onto the argv

txt = open(filename) # here we are opening a file into our script file

print "Here's your file %r." %filename # here it is printing the contents of the opened file

print txt.read() # we are calling a function on txt

print "Type the filename again:" # typing the filename again

file_again = raw_input(">") # taking the input file from the user during the execution

print "the file name entered is",file_again # printing the name of the again entered file

txt_again = open(file_again) # opening the file again on txt

print txt_again.read() # we are calling a function on txt_again
txt.close()