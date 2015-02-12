def read_input_file(fileName):
	with open(str(fileName), "r") as inputFile:
		inputString = inputFile.read()
	return inputString

def output_encode_file(name, inputString):
	with open(str(name + ".hc"), "w") as outputFile:
		outputFile.write(inputString)

def output_decode_file(name, inputString):
	with open(str(name + ".txt"), "w") as outputFile:
		outputFile.write(inputString)