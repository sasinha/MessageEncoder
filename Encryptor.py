import numpy as np
import string
modulo = 26
characterToNumbers=dict(zip(string.ascii_lowercase, range(0,modulo)))

class KeyToMatrix:

    def (self, key):
        keyNumbers = list([characterToNumbers[x] for x in list(key)])
        keyDimension = np.ceil(len(keyNumbers) ** 0.5).astype(int)
        return np.resize(keyNumbers,(keyDimension,keyDimension))





