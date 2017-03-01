from sys import argv

script, user_name = argv
colon = ': '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(colon)

print "Where do you live %s?" % user_name
lives = raw_input(colon)

print "What kind of computer do you have?"
computer = raw_input(colon)

print "What OS do you run?"
operating_system = raw_input(colon)

print """
Alright, so you said %r about liking me.
You live in %r. I know where that is.
And you have a %r computer running %r. Nice
""" % (likes, lives, computer, operating_system)