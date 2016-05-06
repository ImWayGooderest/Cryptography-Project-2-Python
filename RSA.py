from CipherInterface import CipherInterface
import Crypto.PublicKey.RSA
from Crypto.Random import get_random_bytes

class RSA(CipherInterface):
	def __init__(self):
		self.keystring = ""

	def setKey(self, keyfilestring):
		f = open(keyfilestring, 'r')
		Key = f.read()
		if not Key:
			return False

		print(Key)
		self.keystring = Crypto.PublicKey.RSA.importKey(Key)


		return True

	def encrypt(self, plaintext):
		###ciphertext = ""
		###key = self.keystring
		###RSA.importKey(key)
		###f.close()
		###sys.setrecursionlimit(1500)


		k = 535 #The encrypt function requires a random byte string or long parameter that will be ignored
		ciphertext = self.keystring.encrypt(plaintext.encode('utf-8'), 32)
		return ciphertext


	def decrypt(self, ciphertext):
		plaintext = ""
		#key = self.keystring
		#RSA.importKey(key)

		###f.close()
		plaintext = self.keystring.decrypt(ciphertext)
		return plaintext