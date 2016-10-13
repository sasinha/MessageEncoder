import numpy as np
from collections import OrderedDict


def to_matrix(message, dimension, character_string):
    modulo = len(character_string) - 1
    character_to_number = OrderedDict(zip(character_string, range(0, modulo)))
    return np.resize([character_to_number[x] for x in list(message)], dimension)


def to_message(matrix, character_string):
    modulo = len(character_string) - 1
    number_to_character = OrderedDict(zip(range(0, modulo), character_string))
    return ''.join(number_to_character[x] for x in list(np.concatenate(list(matrix))))



# characters = '013456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\x0b2'
# test = to_matrix("013456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW XYZ!", (10, 3), characters)
# testWork = to_message(test, characters)
#
# print(test)
# print(testWork)





