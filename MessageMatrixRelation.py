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

    def __init__(self, message, dimension):  # Create more modulable ToMatrix. Ask for dimension in other package
        self.messageNumbers = list([self.characterToNumber[x] for x in list(message)])
        self.dimension = dimension

    def message_matrix(self):
        return np.resize(self.messageNumbers, self.dimension)


class ToMessage:
    numberToCharacter = dict(zip(range(0, modulo), characters))

    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_message(self):
        return ''.join(numberToCharacter[x] for x in list(np.concatenate(list(self.matrix))))

test = ToMatrix("hello, HoW are you2",(10,10)).message_matrix()
testWork = ToMessage(test).matrix_message()

print(test)
print(testWork)





