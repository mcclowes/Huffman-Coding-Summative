from decoder import *
from encoder import *
from huffman_tools import *

#encodedString = encode_string(process_input(input('\nInput filename (without file suffix):\n') + ".txt"))
#encodedString = encode_string(read_text_file('war_and_peace.txt'))
#encodedString = encode_string(read_text_file('testFile.txt'))

output_encoded_file('output', encode_string(read_text_file('lorum_ipsum2.txt')))
#output_encoded_file('output', encode_string(read_text_file('war_and_peace.txt')))

print ('Decoded: ' + str(read_encoded_file('output.hc')))