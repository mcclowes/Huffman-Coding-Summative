from decoder import *
from encoder import *
from huffman_tools import *
from datetime import datetime

#Take file input
filename = 'lorum_ipsum6'
#filename = 'war_and_peace'
#filename = input('\nInput filename (without file suffix):\n') 

#Encode selected file
startTime = datetime.now()
output_encoded_file(filename, encode_string(read_text_file(filename)))
encodeTime = (datetime.now() - startTime).total_seconds()

#Read encoded file and output decoded text
startTime = datetime.now()
decodedText = read_encoded_file(filename)
decodeTime = (datetime.now() - startTime).total_seconds()
print ('\nDecoded text: \n' + str(decodedText))
output_decoded_file(filename, decodedText)
print ('Encode time: ' + str(encodeTime) + 's\nDecode time: ' + str(decodeTime) + 's')