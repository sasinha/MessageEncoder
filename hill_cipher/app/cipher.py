import numpy as np
from hill_cipher.app import message_matrix_relation as mmr, modulo_inverse_matrix as mim


characters = '0213456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\x0b2'


def encrypt(input_message, dimension):

    modulo = len(characters) - 1
    input_message_matrix_dimension = (dimension, np.ceil(len(input_message) / dimension).astype(int))
    input_message_matrix = mmr.to_matrix(input_message, input_message_matrix_dimension, characters)
    cipher_matrix_dimension = (dimension, dimension)
    cipher_matrix = mim.random_mod_matrix(0, modulo, cipher_matrix_dimension)
    key_matrix = mim.inverse_matrix(cipher_matrix, modulo)
    scrambled_message_matrix = np.mod(np.dot(cipher_matrix, input_message_matrix), modulo)
    return mmr.to_message(scrambled_message_matrix, characters) , mmr.to_message(key_matrix, characters)


def decrypt(input_message, key):

    modulo = len(characters) - 1
    key_matrix_column_length = int(len(key) ** .5)
    key_matrix_dimension = (key_matrix_column_length, key_matrix_column_length)
    scrambled_message_matrix_dimension = (
        key_matrix_column_length, int(np.ceil(len(input_message) / key_matrix_column_length))
    )
    key_matrix = mmr.to_matrix(key, key_matrix_dimension, characters)
    scrambled_message_matrix = mmr.to_matrix(input_message, scrambled_message_matrix_dimension, characters)
    unscrambled_message_matrix = np.mod(np.dot(key_matrix, scrambled_message_matrix), modulo)
    return mmr.to_message(unscrambled_message_matrix, characters)




# Test
if __name__ == "__main__":

    message = "hello, how are you? Lets go meet for dinner / "
    scrambled_message = encrypt(message, 3)
    print(scrambled_message)

    unscrambled_message = decrypt(scrambled_message[0], scrambled_message[1])
    print(unscrambled_message)

