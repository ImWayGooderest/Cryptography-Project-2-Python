from CipherInterface import CipherInterface

class RSA(CipherInterface):
	def __init__(self):
		self.key = ""

	def setKey(self, keyString):
		# code goes here
		return True

	def encrypt(self, plaintext):
		ciphertext = ""
		# code goes here

		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = ""
		# code goes here

		return plaintext
