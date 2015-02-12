import ast

def decode_string(inputString):
	#Convert input file into bit string

	#Read dictionary
	stringDict = inputString[:inputString.index('}')+1]
	bitString = inputString[inputString.index('}')+1:]

	binaryDict = ast.literal_eval(stringDict)
	binaryDict = {v: k for k, v in binaryDict.items()}
	print (binaryDict)
	print (bitString)

	decodedString = binary_to_string(bitString, binaryDict)
	return decodedString

def binary_to_string(inputString, binaryDict):
	outputString = ''
	i = 0
	while i in range(len(inputString)):
		for j in range(i, len(inputString)):
			if (inputString[i:j] in binaryDict):
				#print(inputString[i:j])
				outputString += binaryDict[inputString[i:j]]
				i = j - 1
				break
		i += 1

	return outputString
