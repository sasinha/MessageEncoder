import numpy as np
from ModularInverseMatrix import inverse_matrix

# import string

# modulo = 26
# characters = string.ascii_lowercase  # characters used

characters = '013456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\x0b2'
modulo = len(characters)  # number of characters


def to_matrix(message, dimension):
    character_to_number = dict(zip(characters, range(0, modulo)))
    message_numbers = list([character_to_number[x] for x in list(message)])
    return np.resize(message_numbers, dimension)


def to_message(matrix):
    number_to_character = dict(zip(range(0, modulo), characters))
    return ''.join(number_to_character[x] for x in list(np.concatenate(list(matrix))))

# test = to_matrix("hello, HoW are you2",(10,10))
# testWork = to_message(test)
#
# print(test)
# print(testWork)





