import numpy as np

# import string

# modulo = 26
# characters = string.ascii_lowercase  # characters used

characters = '013456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\x0b2'
modulo = len(characters)  # number of characters
characterToNumber = dict(zip(characters, range(0, modulo)))
numberToCharacter = dict(zip(range(0, modulo), characters))


class ToMatrix:
    characterToNumber = dict(zip(characters, range(0, modulo)))

    def __init__(self, message, dimension):
        self.messageNumbers = list([self.characterToNumber[x] for x in list(message)])
        self.dimension = dimension

    def matrix(self):
        return np.resize(self.messageNumbers, self.dimension)


class ToMessage:
    numberToCharacter = dict(zip(range(0, modulo), characters))

    def __init__(self, matrix):
        self.matrix = matrix

    def message(self):
        return ''.join(numberToCharacter[x] for x in list(np.concatenate(list(self.matrix))))

# test = ToMatrix("hello, HoW are you2",(10,10)).matrix()
# testWork = ToMessage(test).message()
#
# print(test)
# print(testWork)
