from decoder import *
from encoder import *
from huffman_tools import *

#encodedString = encode_string(process_input(input('\nInput filename (without file suffix):\n') + ".txt"))
#encodedString = encode_string(read_input_file('lorum_ipsum.txt'))
encodedString = encode_string(read_input_file('testFile.txt'))
print (encodedString)

#decodedString = decode_string(encodedString)
#print (decodedString)

	