#import 
from sys import argv

#Breaks argv into three arguments to UNPACK 
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

fourth = raw_input("What would be a fourth variable? ")
print "So your fourth variable is: %r" % fourth