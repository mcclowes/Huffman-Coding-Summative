from decoder import *
from encoder import *
from huffman_tools import *
from datetime import datetime

def run(filename):
	print ('> Running on ' + filename)

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
	print ('Encode time: ' + str(encodeTime) + 's\nDecode time: ' + str(decodeTime) + 's\n\n')

run('lorum_ipsum')
run('lorum_ipsum2')
run('lorum_ipsum3')
run('lorum_ipsum4')
run('lorum_ipsum5')
run('lorum_ipsum6')
run('war_and_peace')
#run(input('\nInput filename (without file suffix):\n'))