#Takes a string and encodes in binary
def encode_string(inputString):
	freqCounter = ()
	freqTotal = 0
	#Calculate char probabilities
	for c in inputString:
	    freqCounter[c] += 1
	    freqTotal +=1
	charDict = sorted(freqCounter, key=freqCounter.get)

	#Print freqs for ref
	for c in charDict:
		print '%s %6d' % (c[0], freqCounter[c]/freqTotal)
	charList = charDict.items()
	print charList

	#Calculate correct bit chars
	binaryDict = grow_tree(charList)

	#Output input string as an encoded string
	print (write_binary(binaryDict, inputString))
	#output_encode_file(write_binary(binaryDict, inputString))

#key = letter, value = freq
def grow_tree(charList):
	binaryDict = collections.defaultdict(int)
	for key in charList:
		binaryDict[key] = 2

	#Until tree in completed
	while (len(charList)>1):
		min1 = min(charList)
		charList.remove(min1)
		min2 = min(charList)
		charList.remove(min2)

		#build up binary

	#search?
	#combine two lowest freq elements
	#sort list?
	deconstruct_tree()
	pass
	#return binaryDict

def deconstruct_tree(tree):
	for element in tree:
		pass

def write_binary(binaryDict, inputString):
	binaryString = ''
	for c in inputString:
		binaryString = binaryString + binaryDict[c]
	return binaryString