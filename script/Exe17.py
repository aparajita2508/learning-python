from sys import argv
from os.path import exists # we are importing another handy command from os named exists, it produces either true or false
script, from_file, to_file = argv 
print "copying from %s to %s" %(from_file, to_file) # printing the names, from exist file to new file
in_file = open(from_file) # opening the file for reading
indata = in_file.read() # reading the file
print "The input file is %d bytes long" %len(indata)
print "Does the output file exists? %r" %exists(to_file) # checking if the file exists
print "Ready hit return to continue or CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w') # open the file for writing
out_file.write(indata) # writing data to to file
print "Alright right! all done."
out_file.close() # closing the file resource
in_file.close() # closing the file resource


# import os
# os.path.exist()