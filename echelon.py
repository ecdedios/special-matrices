import numpy as np

def isSingular(A) :
    B = np.array(A, dtype=np.float_)
    try:
        fixRowZero(B)
        fixRowOne(B)
        fixRowTwo(B)
        fixRowThree(B)
    except MatrixIsSingular:
        return True
    return False

class MatrixIsSingular(Exception): pass

def fixRowZero(A) :
    if A[0,0] == 0 :
        A[0] = A[0] + A[1]
    if A[0,0] == 0 :
        A[0] = A[0] + A[2]
    if A[0,0] == 0 :
        A[0] = A[0] + A[3]
    if A[0,0] == 0 :
        raise MatrixIsSingular()
    A[0] = A[0] / A[0,0]
    return A

def fixRowOne(A) :
    A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        raise MatrixIsSingular()
    A[1] = A[1] / A[1,1]
    return A

def fixRowTwo(A) :
    A[2] = A[2] - A[0] * A[2,0]
    A[2] = A[2] - A[1] * A[2,1]
    if A[2,2] == 0 :
        A[2] = A[2] + A[3]
        A[2] = A[2] - A[0] * A[2,0]
        A[2] = A[2] - A[1] * A[2,1]
    if A[2,2] == 0 :
        raise MatrixIsSingular()
    A[2] = A[2] / A[2,2]
    return A

def fixRowThree(A) :
    A[3] = A[3] - A[0] * A[3,0]
    A[3] = A[3] - A[1] * A[3,1]
    A[3] = A[3] - A[2] * A[3,2]    
    if A[3,3] == 0:
        raise MatrixIsSingular()
    A[3] = A[3] / A[3,3]
    return A



# TESTS

A = np.array([
        [2, 0, 0, 0],
        [0, 3, 0, 0],
        [0, 0, 4, 4],
        [0, 0, 5, 5]
    ], dtype=np.float_)
isSingular(A)

A = np.array([
        [1, 1, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)

fixRowZero(A)
fixRowOne(A)
fixRowTwo(A)
fixRowThree(A)