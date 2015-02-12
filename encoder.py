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
	while len(tree) > 1:
	#Sort (indent)
		tree.sort(key=lambda tup: tup[1])
		print (tree)
	#take min1 and min2 and remove
		min1 = tuple(tree[0])
		min2 = tuple(tree[1])
		print ("Min1 = " + str(min1))
		print ("Min2 = " + str(min2))
		del tree[0]
		del tree[0]

	#combine min1 and min2 into a new tuple, with the summed freq
		newTup = ((min1, min2), min1[1] + min2[1])
		print ("new tup" + str(newTup))

	#add in new tuple
		tree.append(newTup)

	#add binary
	binaryDict = {}
	walk_tree(tree[0], binaryDict, '')
	print (binaryDict)

	return output_string(binaryDict, inputString)

def walk_tree(node, dic, code):
	if type(node[0]) == type("str"):
		dic.update({node[0]:code})
	else:
		print ("Current node = " + str(node[0]))
		print ("Node type = " + str(type(node[0])))
		walk_tree(node[0][0], dic, code + '0')
		walk_tree(node[0][1], dic, code + '1')
	return dic

def output_string(binaryDict, inputString):
	output_string = ''
	for char in inputString:
		output_string += binaryDict[char]
	return output_string

		