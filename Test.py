from modulo_inverse_matrix import inverse_matrix
import numpy as np


def test():

    key_matrix = 0
    while key_matrix == 0:
        cipher_matrix = np.random.randint(0, 97, (4, 4))
        key_matrix = inverse_matrix(cipher_matrix, (4, 4))
    else:
        return key_matrix



a=test()

print(a)