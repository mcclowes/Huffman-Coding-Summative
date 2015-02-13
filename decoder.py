import ast
import struct

def decode_string(inputString):
	#Read + convert dictionary
	stringDict = inputString[:inputString.index('}') + 1]
	binaryDict = ast.literal_eval(stringDict)
	binaryDict = {v: k for k, v in binaryDict.items()}

	#convert rest to binary
	restString = inputString[inputString.index('}')+1:]
	bitString = ''
	for byte in restString:
		bitString = bitString + str(byte)

	bitString = map(lambda x: bin(ord(x))[2:], bitString)
	#print ('buffer: ' + str(bitString[0]))
	for i in range(0, len(bitString)):
		while len(bitString[i])<8:
			bitString[i] = '0' + bitString[i]
	#print ('string: ' + str(bitString[1:]))

	#Read buffer counter
	bufferCount = str(bitString[0])
	bufferCount = int(bufferCount,2)
	#print (bufferCount)

	#Join into single string
	bitString = ''.join(bitString[1:])
	#remove buffers
	bitString = bitString[0:-bufferCount]

	decodedString = binary_to_string(bitString, binaryDict)
	return decodedString

#Converts binary into a string
def binary_to_string(inputString, binaryDict):
	outputString = ''
	i = 0
	while i in range(len(inputString) + 1):
		for j in range(i, len(inputString) + 1):
			if (inputString[i:j] in binaryDict):
				#print(inputString[i:j])
				outputString += binaryDict[inputString[i:j]]
				i = j - 1
				break
		i += 1

	return outputString
