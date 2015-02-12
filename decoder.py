import ast
import struct

def decode_string(inputString):
	print ('READING NOW!')
	#Read + convert dictionary
	stringDict = inputString[:inputString.index('}') + 1]
	binaryDict = ast.literal_eval(stringDict)
	binaryDict = {v: k for k, v in binaryDict.items()}
	print (stringDict)

	restString = 

	#Read buffer counter
	bufferCount = 6
	#bufferCount = str(inputString[inputString.index('}')+1:inputString.index('}')+9])
	#print (bufferCount)
	#bufferCount = int(bufferCount,2)
	#print (bufferCount)

	#Read string
	tempString = inputString[inputString.index('}') + 9:-bufferCount]

	#Convert input file into bit string
	bitString = ''
	for i in tempString:
		bitString = bitString + str(i)
	print ('printing bitString ' + str(bitString))

	#into binary again
	bitString = map(lambda x: bin(ord(x))[2:], bitString)
	print (str(bitString[0:9]))
	print (str(bitString[9:]))

	#convert byte to int
	#bufferCount = struct.unpack('B', data[0])[0]

	decodedString = binary_to_string(bitString, binaryDict)
	return decodedString

#Converts binary into a string
def binary_to_string(inputString, binaryDict):
	outputString = ''
	i = 0
	stringEnd = len(inputString)
	while i in (range(stringEnd) + 1):
		for j in range(i, stringEnd + 1):
			if (inputString[i:j] in binaryDict):
				#print(inputString[i:j])
				outputString += binaryDict[inputString[i:j]]
				i = j - 1
				break
		i += 1

	return outputString
