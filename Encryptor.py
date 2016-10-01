import numpy as np
import string


class toMatrix:
    modulo = 26
    characters=string.ascii_lowercase
    characterToNumber=dict(zip(characters, range(0,modulo)))
    numberToCharacter = dict(zip(range(0,modulo), characters))

    def __init__(self, key, message):
        self.keyNumbers = list([self.characterToNumber[x] for x in list(key)])
        self.messageNumbers = list([self.characterToNumber[x] for x in list(key)])
        self.keyDimension = np.ceil(len(self.keyNumbers) ** 0.5).astype(int)

    def keyMatrix(self):
        return np.resize(self.keyNumbers,(self.keyDimension,self.keyDimension))








