Names:
Alberto Gomez	otrebla117@csu.fullerton.edu
Michael Hatcher	lightball20@csu.fullerton.edu
Brendon Hollingsworth	brendonh@csu.fullerton.edu
Trevor Hurt	thurt@csu.fullerton.edu
Akash Raju	zakashx@csu.fullerton.edu

Programming Language: Python 3

How to run the program:
python3.2 cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUTFILE>
DES example: python3.2 cipher.py DES 01234567 ENC test.txt testDESenc.txt
RSA example: python3.2 cipher.py RSA pubkey.pem ENC test.txt testRSAenc.txt

Extra Cred: Not implemented

Special Note:
The key for DES must be 8 bytes.
For RSA, use the pubkey.pem file to encrypt and the privkey.pem to decrypt.
