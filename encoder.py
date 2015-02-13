import collections

#Takes a text string, compresses, and encodes to binary
def encode_string(inputString):
	#Take string and create an array of tuples of characters and their respective frequencies
	charCounter = {}
	for char in inputString:
	  if char in charCounter:
	    charCounter[char] += 1
	  else:
	    charCounter[char] = 1

	#Create a tree
	tree = charCounter.items()
	while len(tree) > 1:
		tree.sort(key=lambda tup: tup[1])
	#Take 2 min elements and remove
		min1 = tuple(tree[0])
		min2 = tuple(tree[1])
		del tree[0]
		del tree[0]

	#Combine min1 and min2 into a new tuple, with the summed freq. Append
		newTup = ((min1, min2), min1[1] + min2[1])
		tree.append(newTup)

	#Create binary values for each char
	binaryDict = {}
	walk_tree(tree[0], binaryDict, '')
	print (binaryDict)

	#Return dictionary(for decoding purposes) + encoded binary of input text
	return str(binaryDict) + string_to_bits(output_string(binaryDict, inputString))

#Traverse tree and generate huffman binary values for each char
def walk_tree(node, binaryDict, binaryCode):
	if type(node[0]) == type("str"):
		binaryDict.update({node[0]:binaryCode})
	else:
		walk_tree(node[0][0], binaryDict, binaryCode + '0')
		walk_tree(node[0][1], binaryDict, binaryCode + '1')
	return binaryDict

def output_string(binaryDict, inputString):
	output_string = ''
	for char in inputString:
		output_string += binaryDict[char]
	return output_string

def string_to_bits(bitString):
	#Ensure bitString is % 8 (pad)
	paddingCounter = 0
	while (len(bitString) % 8 != 0):
		bitString += '0'
		paddingCounter += 1

	#Add buffer length count to front as 1 byte
	paddingCounter = '{0:08b}'.format(paddingCounter)
	bitString = paddingCounter + bitString

	#Divide bitString into array of bytes. Return.
	chunkedString = [bitString[i:i + 8] for i in range(0, len(bitString), 8)]
	return bytearray(map(lambda x: int(x,2), chunkedString))

	
		