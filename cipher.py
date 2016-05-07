import RSA, DES_class
import sys

def handleInput(cipherName, inputKey, encDec, inputFile, outputFile):	###function to handle user input

	if(cipherName == "DES"):
		myCipher = DES_class.DES_class()
		if myCipher.setKey(inputKey):
			if(encDec == "ENC"):
				iFile = open(inputFile).read()
				oFile = open(outputFile, "wb")
				cipherText = myCipher.encrypt(iFile)
				oFile.write(cipherText)
				print("Successfully encrypted with DES!")
			else:
				iFile = open(inputFile, "rb").read()
				oFile = open(outputFile, "wb")
				plainText = myCipher.decrypt(iFile)
				oFile.write(plainText)
				print("Successfully decrypted with DES!")
		else:
			print("Invalid Key!")

	elif(cipherName == "RSA"):
		myCipher = RSA.RSA()
		if myCipher.setKey(inputKey):
			if(encDec == "ENC"):
				print("Encrypting with RSA... (note: may take a while for large files)")
				iFile = open(inputFile).read()
				oFile = open(outputFile, "wb")
				cipherText = myCipher.encrypt(iFile)
				oFile.write(cipherText)
				print("Successfully encrypted with RSA!")
			else:
				print("Decrypting with RSA... (note: may take a while for large files)")
				iFile = open(inputFile, "rb").read()
				oFile = open(outputFile, "wb")
				plainText = myCipher.decrypt(iFile)
				oFile.write(plainText)
				print("Successfully decrypted with RSA!")
		else:
			print("Invalid Key!")

	else:
		print("Invalid Cipher Name! Use:\nDES: DES\n RSA: RSA")

def main():
	handleInput(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])


if __name__ == "__main__":
	main()