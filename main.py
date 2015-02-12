from decoder import *
from encoder import *
from huffman_tools import *

#encodedString = encode_string(process_input(input('\nInput filename (without file suffix):\n') + ".txt"))
encodedString = encode_string(read_input_file('lorum_ipsum.txt'))
#encodedString = encode_string(read_input_file('war_and_peace.txt'))
#encodedString = encode_string(read_input_file('testFile.txt'))
with open('output.hc', 'wb') as encodeFile:
	encodeFile.write(encodedString)
print ("Encoded string.")

with open('output.hc', 'rb') as decodeFile:
	print decode_string(decodeFile.read())

#decodedString = decode_string(encodedString)
#print ("Decoded string = " + str(decodedString))

	