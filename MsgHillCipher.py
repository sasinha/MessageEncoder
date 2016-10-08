#!usr/bin/python3
import MessageMatrixRelation.py
import string

char=list(string.ascii_lowercase)

operationType = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
message = input("What is your message? ") + "//"
key = input("What is your key? ")

if operationType == 'e':
    encrypted = encrypt(message,key)
    print("Encrypted message: ", encrypted.scrambled_message)

elif operationType == 'd':
    decrypted = decrypt(message, key)






