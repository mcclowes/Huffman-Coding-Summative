from encoder import *
from decoder import *

def read_text_file(fileName):
	with open(str(fileName + '.txt'), "r") as inputFile:
		inputString = inputFile.read()
	print ("Text file read")
	print ("Text file char count: " + str(len(inputString)))
	return inputString

def output_encoded_file(name, inputString):
	with open(str(name + ".hc"), "wb") as outputFile:
		outputFile.write(inputString)
	print ("Text file encoded")

def read_encoded_file(fileName):
	with open(str(fileName + '.hc'), "rb") as inputFile:
		inputString = inputFile.read()
	print ("Encoded file read")
	decoded = decode_string(inputString)
	print ("Decoded text char count: " + str(len(decoded)))
	return decoded

def output_decoded_file(name, inputString):
	with open(str(name + ".txt"), "w") as outputFile:
		outputFile.write(inputString)
	print ("Encoded file decoded")