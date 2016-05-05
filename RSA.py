from CipherInterface import CipherInterface
from Crypto.PublicKey import RSA
import sys

class RSA(CipherInterface):
	def __init__(self):
		self.keystring = ""

	def setKey(self, keyfilestring):
		f = open(keyfilestring, 'r')
		Key = f.read()
		f.close()
		if not Key:
			return False
		self.keystring = Key
		return True

	def encrypt(self, plaintext):
		###ciphertext = ""
		###key = self.keystring
		###RSA.importKey(key)
		###f.close()
		###sys.setrecursionlimit(1500)
		k = 535 #The encrypt function requires a random byte string or long parameter that will be ignored
		ciphertext = RSA.encrypt(plaintext, k)
		return ciphertext

	def decrypt(self, ciphertext):
		plaintext = ""
		key = self.keystring
		RSA.importKey(key)

		###f.close()
		plaintext = RSA.decrypt(ciphertext)
		return plaintext