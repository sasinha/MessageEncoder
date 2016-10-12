import numpy as np


#  copy-pasted from old cipher and needs cleanup
def inverse_matrix(inputMatrix,modulo):
    a = inputMatrix
    m = modulo
    p = np.round(np.linalg.det(a) * np.linalg.inv(a))
    a = np.round(np.linalg.det(a))
    num = np.arange(1, m + 1)  # creates a modulo dictionary
    res = np.mod(a * num, m)
    b = np.where(res == 1)
    err = np.size(b)
    if err == 0:
        # print("The matrix has no modular inverse")
        return err
    b = b[0].item(0) + 1
    return np.mod(b * p, m).astype(int)


def random_mod_matrix(min, max, dimension):
    random_matrix = np.random.randint(min,max, dimension)
    inverse_mod_matrix = inverse_matrix(random_matrix, max)
    if inverse_mod_matrix == 0:
        random_mod_matrix(min, max, dimension)
    else:
        return random_matrix, inverse_mod_matrix






# Uncomment below for test


#
# mTest=np.array(([6,24,1],[13,16,10],[20,17,15]))
# mResult = np.array(([8,5,10],[21,8,21],[21,12,8]))
# mInverse=inverse_matrix(mTest,26)
# print("Inverse: ", mInverse)
# print("result: ", mResult)


test, testv = random_mod_matrix(0,28,(3,3))
testvv = inverse_matrix(test, 28)

print(test)
print(testv)
print(testvv)
