#!usr/bin/python3
import MessageMatrixRelation.py

char=list(string.ascii_lowercase)

operationType = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
message = input("What is your message? ").lower()
key = input("What is your key? ").lower()
if operationType == "e":
    print(MessageMatrixRelation.scrambledMessage)
else:
    print(Decryptor.unscrambledMessage)





