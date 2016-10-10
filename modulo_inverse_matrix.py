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

# Uncomment below for test


#
# mTest=np.array(([6,24,1],[13,16,10],[20,17,15]))
# mResult = np.array(([8,5,10],[21,8,21],[21,12,8]))
# mInverse=inverse_matrix(mTest,26)
# print("Inverse: ", mInverse)
# print("result: ", mResult)




def test():
    modulo = 27
    c = 0
    while c == 0:
        A = np.random.randint(0, modulo, (4, 4))
        b = inverse_matrix(A, modulo)
        c = b.all()
        if c != 0:
            return b

b=test()
print(b)
