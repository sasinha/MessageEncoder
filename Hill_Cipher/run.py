#!usr/bin/python3

from Hill_Cipher import cipher

operationType = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
message = input("What is your message? ") + " // "

if operationType == 'e':
    dimension = int(input("What dimension would you like your key to be? "))
    encrypted = cipher.encrypt(message, dimension)
    print("Encrypted message: ", encrypted[0])
    print("Key: ", encrypted[1])

elif operationType == 'd':
    key = input("What is your key? ")
    decrypted = cipher.decrypt(message, key)
    print("Unscrambled message: ", decrypted)






