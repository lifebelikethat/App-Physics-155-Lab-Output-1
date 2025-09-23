import numpy as np

A = np.array([4., 4, 8, 4, 4, 5, 3, 7, 8,
              3, 9, 9, 4, 7, 9, 5]).reshape(4, 4)
bs = np.array([1., 2, 3, 4])


def backsub(U,bs):
    n = bs.size
    xs = np.zeros(n)
    for i in reversed(range(n)):
        xs[i] = (bs[i] - U[i,i+1:]@xs[i+1:])/U[i,i]
    return xs


def gauelim(mtrx, mtrx2):
    A = np.copy(mtrx)
    bs = np.copy(mtrx2)
    n = bs.size

    for j in range(n-1):
        for i in range(j+1, n):
            coeff = A[i,j] / A[j,j]
            A[i,j:] -= coeff*A[j,j:]
            bs[i] -= coeff*bs[j]

    xs = backsub(A, bs)
    return xs


def gauelim2(mtrx, mtrx2):
    A = np.copy(mtrx)
    bs = np.copy(mtrx2)
    n = bs.size

    for j in range(n-1):
        for i in range(j+1, n):
            if A[j,j] == 0:
                A[j,j] = 1e-20

            coeff = A[i,j] / A[j,j]
            A[i,j:] -= coeff*A[j,j:]
            bs[i] -= coeff*bs[j]

    xs = backsub(A, bs)
    return xs



def gauelim_pivot(mtrx1, mtrx2):
    A = np.copy(mtrx1)
    bs = np.copy(mtrx2)
    n = bs.size

    for j in range(n-1):
        for i in range(j+1, n):
            coeff = A[i,j] / A[j,j]
            A[i,j:] -= coeff*A[j,j:]
            bs[i] -= coeff*bs[j]

    xs = backsub(A, bs)
    return xs


def gauelim_pivot2(mtrx1, mtrx2):
    A = np.copy(mtrx1)
    bs = np.copy(mtrx2)
    n = bs.size

    for j in range(n-1):
        for i in range(j+1, n):
            if A[j,j] == 0:
                A[j,j] = 1e-20

            coeff = A[i,j] / A[j,j]
            A[i,j:] -= coeff*A[j,j:]
            bs[i] -= coeff*bs[j]

    xs = backsub(A, bs)
    return xs

# returns nan since matrix is nearly singular -2.19e-14
print(gauelim(A, bs))
print(gauelim_pivot(A, bs))

'''
replacing U_ii = 0 with U_ii = 1e-20 gives the same
result since the matrix is singular
'''
print(gauelim2(A, bs))
print(gauelim_pivot2(A, bs))

