from message_matrix_relation import to_matrix, to_message
from modulo_inverse_matrix import inverse_matrix, random_mod_matrix
import numpy as np

characters = 'abcdefghijklmnopqrstuvwxyz /"'
# class Cipher:
#
#     def __init__(self, input_message):
#
#         # self.characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\x0b'
#         self.characters = 'abcdefghijklmnopqrstuvwxyz /"'
#         self.modulo = len(self.characters) - 1
#         self.input_message = input_message
#         self.input_message_matrix = to_matrix(input_message, input_message_matrix_dimension, self.characters)
#
#     def encrypt(self,dimension):
#         self.cipher_matrix_dimension = (dimension, dimension)
#         input_message_matrix_dimension = (dimension, np.ceil(len(self.input_message) / dimension).astype(int))
#         cipher_matrix = np.random.randint(0, self.modulo, self.cipher_matrix_dimension)
#         key_matrix = inverse_matrix(cipher_matrix, self.modulo)
#         scrambled_message_matrix = np.mod(np.dot(cipher_matrix, self.input_message_matrix), self.modulo)
#         return to_message(scrambled_message_matrix, self.characters), to_message(key_matrix, self.characters)
#
#     def decrypt(self, key):
#         unscrambled_message_matrix = np.mod(np.dot(self.key_matrix, self.input_message_matrix), self.modulo)
#         return to_message(unscrambled_message_matrix, self.characters)


def encrypt(input_message, dimension):

    modulo = len(characters) - 1
    input_message_matrix_dimension = (dimension, np.ceil(len(input_message) / dimension).astype(int))
    input_message_matrix = to_matrix(input_message, input_message_matrix_dimension, characters)
    cipher_matrix_dimension = (dimension, dimension)
    (cipher_matrix, key_matrix) = (random_mod_matrix(0,modulo,cipher_matrix_dimension))
    scrambled_message_matrix = np.mod(np.dot(cipher_matrix, input_message_matrix), modulo)
    return to_message(scrambled_message_matrix, characters), to_message(key_matrix, characters)


def decrypt(input_message, key):
    modulo = len(characters) - 1
    key_matrix_column_length = len(key) ** .5
    key_matrix_dimension = (key_matrix_column_length, key_matrix_column_length)
    scrambled_message_matrix_dimension = (
        key_matrix_column_length, np.ceil(len(input_message) / key_matrix_column_length)
    )
    key_matrix = to_matrix(key, key_matrix_dimension, characters)
    scrambled_message_matrix = to_matrix(input_message, scrambled_message_matrix_dimension, characters)
    unscrambled_message_matrix = np.mod(np.dot(key_matrix, scrambled_message_matrix), modulo)
    return to_message(unscrambled_message_matrix, characters)




# Test

message = "hello how are / "
scrambled_message = encrypt(message, 3)
print(scrambled_message)

# unscrambled_message = decrypt(scrambled_message[0], scrambled_message[1])
# print(unscrambled_message)

