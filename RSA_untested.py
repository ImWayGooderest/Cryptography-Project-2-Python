from CipherInterface import CipherInterface
from Crypto.PublicKey import RSA

class RSA_433(CipherInterface):
	def __init__(self):
		self.keyfile = ""

	def setKey(self, keyfilestring):
		self.keyfile = keyfilestring
		RSA.generate(2048)
		f = open(keyfilestring, 'w')
		f.write(RSA.exportKey('PEM'))
		f.close()
		return True

	def encrypt(self, plaintext):
		ciphertext = ""
		keyfilestring = self.keyfile
		f = open(keyfilestring,  'r')
		RSA.importKey(f.read()))
		f.close()
		k = 535 #The encrypt function requires a random byte string or long parameter that will be ignored
		ciphertext = RSA.encrypt(plaintext, k)
		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = ""
		keyfilestring = self.keyfile
		f = open(keyfilestring,  'r')
		RSA.importKey(f.read()))
		f.close()
		plaintext = RSA.decrypt(ciphertext)
		return plaintext
