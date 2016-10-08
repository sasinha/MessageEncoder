import MessageMatrixRelation
import numpy as np

class Cipher:

    def __init__(self, input_message, key):
        key_matrix_column_length = np.ceil(len(key) ** .5)
        key_matrix_dimension = (key_matrix_column_length, key_matrix_column_length)
        message_matrix_dimension = (key_matrix_column_length, np.ceil(len(key) / key_matrix_column_length))
        self.input_message_matrix = to_matrix(input_message, message_matrix_dimension)
        self.key_matrix = to_matrix(key, key_matrix_dimension)

    def encrypt(self):
        cipher_matrix = inverse_matrix(self.key_matrix, modulo)
        scrambled_message_matrix = np.mod(np.dot(cipher_matrix, self.input_message_matrix), modulo)
        return to_message(scrambled_message_matrix)

    def decrypt(self):
        unscrambled_message_matrix = np.mod(np.dot(self.key_matrix, self.input_message_matrix), modulo)
        return to_message(unscrambled_message_matrix)