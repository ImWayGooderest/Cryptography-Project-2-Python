from CipherInterface import CipherInterface

class DES(CipherInterface):
	def __init__(self):
		self.key = ""

	def setKey(self, keyString):
		# code goes here
		return True

	def encrypt(self, plaintext):
		ciphertext = ""
		# code stuff goes here

		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = ""
		# code stuff goes here

		return plaintext