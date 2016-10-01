
import numpy as np

class ModularInverseMatrix:
    def modularInverseMatrix(matrix,modulo=26):
    #Inverted modulus matrix subroutine
    # P=np.round(np.linalg.det(matrix)*np.linalg.inv(matrix))
    a=np.round(np.linalg.det(matrix))
    num=np.arange(1,modulo+1) #creates a modulo dictionary
    res=np.mod(a*num, modulo)
    b=np.where(res==1)
    err=np.size(b)
    if err == 0:
        print("The randomly generated cipher matrix is not modulable")
        return
    b=b[0].item(0)+1
    return np.mod(b*P,modulo).astype(int)
