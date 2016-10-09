from message_matrix_relation import to_matrix, to_message
from modulo_inverse_matrix import inverse_matrix
import numpy as np


class Cipher:

    def __init__(self, input_message, dimension):

        # self.characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\x0b'
        self.characters = 'abcdefghijklmnopqrstuvwxyz /"'
        self.modulo = len(self.characters) - 1
        self.cipher_matrix_dimension = (dimension, dimension)
        input_message_matrix_dimension = (dimension, np.ceil(len(input_message) / dimension).astype(int))
        self.input_message_matrix = to_matrix(input_message, input_message_matrix_dimension, self.characters)

    def encrypt(self):
        cipher_matrix = np.random.randint(0, self.modulo, self.cipher_matrix_dimension)
        key_matrix = inverse_matrix(cipher_matrix, self.modulo)
        scrambled_message_matrix = np.mod(np.dot(cipher_matrix, self.input_message_matrix), self.modulo)
        return to_message(scrambled_message_matrix, self.characters), to_message(key_matrix, self.characters)

    def decrypt(self):
        unscrambled_message_matrix = np.mod(np.dot(self.key_matrix, self.input_message_matrix), self.modulo)
        return to_message(unscrambled_message_matrix, self.characters)


# Test

message = "hello how are / "
password = "supsdsdfgff "
scrambled_message = Cipher(message, 3).encrypt()
print(scrambled_message)
print(len(message), len(password), len(scrambled_message))

unscrambled_message = Cipher(scrambled_message,password).decrypt()
print(unscrambled_message)

