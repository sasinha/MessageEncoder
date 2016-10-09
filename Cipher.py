from message_matrix_relation import to_matrix, to_message
from modulo_inverse_matrix import inverse_matrix
import numpy as np


class Cipher:

    def __init__(self, input_message, key):

        self.characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\x0b'

        self.modulo = len(self.characters) - 1
        if
        key_matrix_column_length = np.ceil(len(key) ** .5).astype(int)
        key_matrix_dimension = (key_matrix_column_length, key_matrix_column_length)
        message_matrix_dimension = (key_matrix_column_length, np.ceil(len(key) / key_matrix_column_length).astype(int))
        self.input_message_matrix = to_matrix(input_message, message_matrix_dimension, self.characters)
        self.key_matrix = to_matrix(key, key_matrix_dimension, self.characters)

    def encrypt(self):
        cipher_matrix = inverse_matrix(self.key_matrix, self.modulo)
        scrambled_message_matrix = np.mod(np.dot(cipher_matrix, self.input_message_matrix), self.modulo)
        return to_message(scrambled_message_matrix, self.characters)

    def decrypt(self):
        unscrambled_message_matrix = np.mod(np.dot(self.key_matrix, self.input_message_matrix), self.modulo)
        return to_message(unscrambled_message_matrix, self.characters)


# Test

message = "Hello / "
password = "itit"
scrambled_message = Cipher(message,password).encrypt()
print(scrambled_message)
print(len(message), len(password), len(scrambled_message))

unscrambled_message = Cipher(scrambled_message,password).decrypt()
print(unscrambled_message)

