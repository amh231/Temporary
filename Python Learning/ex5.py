#Variables Assigned
name = 'Allyn Heft'
age = 23
height = 75 #inches
weight = 215
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

#Print Stuff 
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Acutally that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)