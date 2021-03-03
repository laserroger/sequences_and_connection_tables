'''
	(c) Enrique Mendez, 2020

	Contains functions for helping with extracting data from the Photon Counting
	cards produced .LST files. Extracted from my old work on the blacs_worker.py
	in the P7888 device in user_devices.
'''

def determine_newline_type(self, entire_file):
	'''newline_type, newline = determine_newline_type(entire_file)

	Reads a whole file in as a string and returns newline type as string 'CRLF',
	'CR', 'LF' as well as the newline string.
	'''
	if(b'\r\n' in entire_file):
		print("Contains CRLF")
		newline_type = 'CRLF'
		newline = b'\r\n'
	elif(b'\r' in entire_file):
		print("Contains CR")
		newline_type = 'CR'
		newline = b'\r'
	elif(b'\n' in entire_file):
		print("Contains LF")
		newline_type = 'LF'
		newline = b'\n'

	return (newline_type, newline)

def split_file_into_header_and_data(self, entire_file, newline):
	''' header, data = split_file_into_header_and_data(entire_file, newline) 

	entire_file is a binary string.

	Reads entire file to find the start of the data '[DATA]' and
	then looks a newline after it to find the datastream.
	'''

	#find the start of the data and split the .lst file
	data_marker = entire_file.find(b'[DATA]')
	data_start = data_marker + len(b'[DATA]') + len(newline)
	header = entire_file[0:data_start]
	data = entire_file[data_start:]

	return header, data

def decode_data(self, data,verbose=False):
	''' channels, quantized_times = decode_data(data)
	
	data is a binary string.

	Deconverts the bytes into python-computable integer lists. Data is encoded 
	as a LSB first and as decoded as such.

	Channel Values are from 0 to 3 inclusive. Denoting the 4 input channels.
	The Start events are encoded in one of these channels, and denoted by
	the 0 timing and non-zero channel.

	Quantized times are in units found in the header file.

	Verbose print's the decoded data in binary format.
	'''

	if len(data) % 4 != 0:
		raise RuntimeError("Error: P7888 data isn't in 32 bit chunks")

	number_of_32_bit_chunks = len(data)//4

	datalines	= [None] * number_of_32_bit_chunks
	dataints 	= np.zeros(number_of_32_bit_chunks, dtype=np.int64)

	for i in range(number_of_32_bit_chunks):
		datalines[i]	= data[4*i:4*(i+1)]
		dataints[i] 	= int.from_bytes(datalines[i], byteorder='little')

	#seperate the first four bits (data is now in Most Significant Bit First).
	channels       	= np.zeros(number_of_32_bit_chunks, dtype=np.int32)
	quantized_times	= np.zeros(number_of_32_bit_chunks, dtype=np.int32)

	for i in range(number_of_32_bit_chunks):
		channels[i]       	= dataints[i] >> 30	
		quantized_times[i]	= (0xffFFffFF >> 2) & dataints[i]
		if verbose:
			print("0b{:02b}:{:030b}".format(channels[i],quantized_times[i]))

	return channels, quantized_times

def decode_header(self, header, verbose=False):
	''' dictionary = decode_header(header)

	header is binary string.

	Takes the header datastream and splits it into keys and values in
	dictionary.

	All values are strings.

	'''

	dictionary = {}

	header = header.decode('utf-8')	#convert bytestream to string
	header = header.splitlines()   	#break up into line by line.

	#remove the datafile timestamp before extracting keys and values.
	dictionary['timestamp'] = header.pop()

	for line in header:
		if line[0] == ';':
			#skip commented lines.
			continue
		if '=' in line:
			split_line = line.split('=')
		else:
			split_line = line.split(':')

		#strip removes leading and trailing whitespace.
		dictionary[split_line[0]] = split_line[1].strip()

	if verbose:
		print(dictionary)
	
	return dictionary