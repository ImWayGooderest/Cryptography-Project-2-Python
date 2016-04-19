from CipherInterface import CipherInterface
from Crypto.Cipher import DES

class DES_class(CipherInterface):
	def __init__(self):
		self.key = ""
		self.des = ""

	def setKey(self, keyString):
		# code goes here
		keyString = bytes(keyString, encoding="ascii")
		if(len(keyString)):
			self.key = keyString
			return True
		else:
			return False

	def encrypt(self, plaintext):
		ciphertext = ""
		self.des = DES.new(self.key, DES.MODE_ECB)
		# code stuff goes here
		ciphertext = self.des.encrypt(plaintext)
		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = ""
		# code stuff goes here
		plaintext = self.des.decrypt(ciphertext)
		return plaintext