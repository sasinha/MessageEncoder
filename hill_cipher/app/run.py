#!usr/bin/python3
from app import operation as op

operationType = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
message = input("What is your message? ") + " // "
answer = op.cipher_operation(operationType, message)


