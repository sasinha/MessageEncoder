import numpy as np
import string

modulo = 26  # number of characters
characters = string.ascii_lowercase  # characters used
characterToNumber = dict(zip(characters, range(0, modulo)))
numberToCharacter = dict(zip(range(0, modulo), characters))


class ToMatrix:

    characterToNumber = dict(zip(characters, range(0, modulo)))

    def __init__(self, key, message):  # Create more modulable ToMatrix. Ask for dimension in other package
        self.keyNumbers = list([self.characterToNumber[x] for x in list(key)])
        self.messageNumbers = list([self.characterToNumber[x] for x in list(key)])
        self.keyDimension = np.ceil(len(self.keyNumbers) ** 0.5).astype(int)
        self.messageRowSize = np.ceil(len(self.messageNumbers) / self.keyDimension)

    def key_matrix(self):
        return np.resize(self.keyNumbers, (self.keyDimension, self.keyDimension))

    def message_matrix(self):
        return np.resize(self.messageNumbers, (self.keyDimension, self.messageRowSize))


class ToMessage:
    numberToCharacter = dict(zip(range(0, modulo), characters))

    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_message(self):
        return ''.join(numberToCharacter[x] for x in list(np.concatenate(list(self.matrix))))

test = ToMatrix("aaaa","hello").message_matrix()
testWork = ToMessage(test).matrix_message()

print(testWork)





