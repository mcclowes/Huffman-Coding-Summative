import ast

def decode_string(inputString):
	#Convert input file into bit string

	#Read dictionary
	stringDict = inputString[:inputString.index('}')+1]
	bitString = inputString[inputString.index('}')+1:]

	binaryDict = ast.literal_eval(stringDict)
	print (binaryDict)
	print (bitString)

	print ('Decoded string = ' + str(binary_to_string(bitString, binaryDict)))

def binary_to_string(inputString, binaryDict):
	outputString = ''
	for i in range(len(inputString)):
		for j in range(i, len(inputString)):
			if (inputString[i:j] in binaryDict):
				outputString += inputString[i:j]
				break

	return outputString
