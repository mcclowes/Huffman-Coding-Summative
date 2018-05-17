# huffman-coding
  
## Using the code
    Note: Code is in Python, version 2.7
Main.py contains the method run() which takes a given filename and reads, encodes, and decodes the associated text file. To run the program, open and run main.py in Idle on a networked machine.
The code will prompt the user to enter a string corresponding to a .txt file to be decoded. This file must be in the same directory as the program .py files. An example file lorum_ipsum.txt has been included in the directory for demonstration purposes.

## The Code
Main.py is the main file which takes input and calls the relevant encoding and decoding methods from external python files encoder.py and decoder.py. I/O handling is done through huffman_tools.py. The main method also uses datetime to evaluate the run time.

The text is encoded by calling encode_string() from encoder.py, which is passed the given text file as a single string (processed in huffman_tools.py) in main.py. Firstly a dictionary is generated containing each character that appears in the text and the frequency with which they appear. This dictionary is then copied into tree and used to build a huffman tree by combining the two smallest frequency elements over and over.

Once the tree is completed, walk_tree() is then called which passes through the tree in order to generate the unique binary key for each character – the crux of the huffman coding technique. With this binary dictionary, the string is converted into first binary, which is then padded and turned into bytes in string_to_bits(). The number of bits used to pad the byte array is added as an initial byte. This byte array is concatenated with the dictionary (which is needed for decoding) and saved to the appropriate output file (<input filename>.hc).

Decoding simply reverses this process. The compressed file is read and passed to decode_string() where the dictionary is sliced off the front of the input and recreated, the padding size (bufferCount) found, and the remaining bytes converted into a string of 1/0s. The padding bits are removed and this string is converted into the correct characters again using the dictionary. Because the tree creates unique binary keys for each character and no key contains another as a substring, there is no risk of mistranslating.
