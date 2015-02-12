import collections

#Takes a string and encodes in binary
def encode_string(inputString):
	#Take string and create an array of tuples of characters and their respective frequencies
	charCounter = {}
	for s in inputString:
	  if charCounter.has_key(s):
	    charCounter[s] += 1
	  else:
	    charCounter[s] = 1

	for key in charCounter:
	  if charCounter[key] > 1:
	    print key, charCounter[key]

	#Copy into a tree
	tree = charCounter.items()
	print (tree)
	#While the tree is bigger than 1
	#while len(tree) > 1:
	#Sort

	#take min1 and min2

	#combine min1 and min2 into a new tuple, with the summed freq
	
	#add in new tuple

	#add binary 