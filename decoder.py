import ast
import struct

def decode_string(inputString):
	#Read, reverse and remove dictionary
	binaryDict = ast.literal_eval(inputString[:inputString.index('}') + 1])
	binaryDict = {v: k for k, v in binaryDict.items()}

	#Convert rest of input (buffer counter + string) to binary
	restString = inputString[inputString.index('}')+1:]
	bitString = ''
	for byte in restString:
		bitString = bitString + str(byte)
	bitString = map(lambda x: bin(ord(x))[2:], bitString)
	for i in range(0, len(bitString)):
		while len(bitString[i])<8:
			bitString[i] = '0' + bitString[i]
	print ('string: ' + str(bitString[1:])) #Correct form

	#Read buffer counter
	bufferCount = str(bitString[0])
	bufferCount = int(bufferCount,2)
	print ("Buffer counter: " + str(bufferCount))

	#Join into single string + remove buffer digits from end
	bitString = ''.join(bitString[1:])
	bitString = bitString[:-bufferCount]

	#Decode into text. Return
	return binary_to_string(bitString, binaryDict)

#Converts binary back into text
def binary_to_string(inputString, binaryDict):
	outputString = ''
	i = 0
	while i in range(len(inputString) + 1):
		for j in range(i, len(inputString) + 1):
			if (inputString[i:j] in binaryDict):
				outputString += binaryDict[inputString[i:j]]
				#print ("i : " + str(i) + " and j : " + str(j))
				i = j - 1
				break
		i += 1
	return outputString
