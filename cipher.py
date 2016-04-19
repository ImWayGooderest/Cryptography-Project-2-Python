import RSA, DES
import sys

def handleInput(cipherName, inputKey, encDec, inputFile, outputFile):	###function to handle user input
	iFile = open(inputFile).read()
	oFile = open(outputFile, "w")

	#The code below is from the last project. I kept it here as an example because I bet this part will be similar for this project
	# if(cipherName == "PLF"):	###Playfair cipher
	# 	myCipher = Playfair.Playfair()
	# 	if myCipher.setKey(inputKey):
	# 		if(encDec == "ENC"):
	# 			cipherText = myCipher.encrypt(iFile)
	# 			oFile.write(cipherText)
	# 		else:
	# 			plainText = myCipher.decrypt(iFile)
	# 			oFile.write(plainText)
	# 	else:
	# 		print("Invalid Key!")
	#
	# elif(cipherName == "RTS"):	###Row Transposition cipher
	# 	myCipher = RowTransposition.RowTransposition()
	# 	if myCipher.setKey(inputKey):
	# 		if(encDec == "ENC"):
	# 			cipherText = myCipher.encrypt(iFile)
	# 			oFile.write(cipherText)
	# 		else:
	# 			plainText = myCipher.decrypt(iFile)
	# 			oFile.write(plainText)
	# 	else:
	# 		print("Invalid Key!")

	# else:
	# 	print("Invalid Cipher Name! Use:\nPLF: PLayfair\n RTS: Row Transposition\nRFC: Railfence\nVIG: Vigenre\nCES: Caesar\nMAC: Monoalphabetic Cipher")

def main():
	if(len(sys.argv) == 6):
		handleInput(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	else:
		print("Invalid number of arguments!\nUSAGE:\npython cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>")


if __name__ == "__main__":
	main()