from decoder import *
from encoder import *
from huffman_tools import *

#Take file input
#filename = 'lorum_ipsum2'
filename = 'war_and_peace'
#filename = input('\nInput filename (without file suffix):\n') 

#Encode selected file
output_encoded_file(filename, encode_string(read_text_file(filename)))

#Read encoded file and output decoded text
print ('\nDecoded text: \n' + str(read_encoded_file(filename)))