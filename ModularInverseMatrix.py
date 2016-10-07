import numpy as np


class ModularInverseMatrix:
    def __init__(self, matrix, modulo):
        self.inputMatrix = matrix
        self.modulo = modulo

    #  copy-pasted from old cipher and needs cleanup
    def inverse_matrix(self):
        a = self.inputMatrix
        m = self.modulo
        p = np.round(np.linalg.det(a) * np.linalg.inv(a))
        a = np.round(np.linalg.det(a))
        num = np.arange(1, m + 1)  # creates a modulo dictionary
        res = np.mod(a * num, m)
        b = np.where(res == 1)
        err = np.size(b)
        if err == 0:
            print("The matrix has no modulable inverse")
            return
        b = b[0].item(0) + 1
        return np.mod(b * p, m).astype(int)

# Uncomment below for test

# mTest=np.array(([6,24,1],[13,16,10],[20,17,15]))
# mResult = np.array(([8,5,10],[21,8,21],[21,12,8]))
# mInverse=ModularInverseMatrix(mTest,26).inverseMatrix()
# print(mInverse)
# print(mResult)

