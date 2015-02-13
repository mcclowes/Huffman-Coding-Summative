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

	#Copy into a tree
	tree = charCounter.items()
	#print (tree)

	#While the tree is bigger than 1
	while len(tree) > 1:
	#Sort (indent)
		tree.sort(key=lambda tup: tup[1])
		#print (tree)
	#take min1 and min2 and remove
		min1 = tuple(tree[0])
		min2 = tuple(tree[1])
		del tree[0]
		del tree[0]

	#combine min1 and min2 into a new tuple, with the summed freq
		newTup = ((min1, min2), min1[1] + min2[1])

	#add in new tuple
		tree.append(newTup)

	#add binary
	binaryDict = {}
	walk_tree(tree[0], binaryDict, '')
	#print (binaryDict)

	return str(binaryDict) + string_to_bits(output_string(binaryDict, inputString)) #add in dictionary too
	#return (str(binaryDict) + str(output_string(binaryDict, inputString)))

def walk_tree(node, dic, code):
	if type(node[0]) == type("str"):
		dic.update({node[0]:code})
	else:
		walk_tree(node[0][0], dic, code + '0')
		walk_tree(node[0][1], dic, code + '1')
	return dic

def output_string(binaryDict, inputString):
	output_string = ''
	for char in inputString:
		output_string += binaryDict[char]
	return output_string

def string_to_bits(bitString):
	#ensure bitString is % 8 (pad)
	paddingCounter = 0
	while (len(bitString) % 8 != 0):
		bitString += '0'
		paddingCounter += 1

	#add buffer length to front
	paddingCounter = '{0:08b}'.format(paddingCounter)
	bitString = paddingCounter + bitString

	#divide bitString into array of bytes
	n = 8
	chunkedString = [bitString[i:i + n] for i in range(0, len(bitString), n)]
	#print (chunkedString)

	#Return converted to bytes
	return bytearray(map(lambda x: int(x,2), chunkedString))

	
		