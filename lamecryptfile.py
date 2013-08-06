import random

class LamecryptFile:

	def __init__(self, path, mode):
		self.__f = open(path, mode)
			
		if mode == 'w':
			# Generate the mask and write it to the file
			self.__mask = random.randint(0, 255)
			self.__f.write( chr(self.__mask) )
		elif mode == 'r':
			# Read the mask from the file
			mask = self.__f.read(1)
			if len( mask ) > 0:
				self.__mask = ord(mask)


	def read(self, size = -1):
		data = self.__f.read(size)
	
		return self.__crypt(data)


	def write(self, data):
		encdata = self.__crypt(data)

		self.__f.write(encdata)


	def __crypt(self, data):
		encdata = ''
		for i in range( len( data ) ):
			encdata += chr( ord(data[i]) ^ self.__mask )

		return encdata


	def close(self):
		self.__f.close()
