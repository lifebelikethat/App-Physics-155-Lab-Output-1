import numpy as np


A = np.array([[9, 2, 3], [1, 12, 9], [4, 6, 14]])
B = np.array([7, 2, 1])

def termcrit(xolds,xnews):
    errs = np.abs((xnews - xolds)/xnews)
    return np.sum(errs)


def jacobi(mtrx1, mtrx2, x0=None, kmax=50, tol=1.e-6):
    A = np.copy(mtrx1)
    bs = np.copy(mtrx2)
    n = bs.size

    if x0 is None:
        xnews = np.zeros(n)
    else:
        xnews = np.copy(x0)

    for k in range(1, kmax):
        xs = np.copy(xnews)

        for i in range(n):
            slt = A[i,:i]@xs[:i]
            sgt = A[i,i+1:]@xs[i+1:]
            xnews[i] = (bs[i] - slt - sgt)/A[i,i]

        err = termcrit(xs, xnews)
        print(k, xnews, err)
        if err < tol:
            break
    return xnews


def tri_diag(a, b, size):
    A = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if i == j:
                A[i,j] = a
            elif (j == i-1) or (j == i+1):
                A[i,j] = b
            else:
                A[i,j] = 0

    A[0, size-1] = b
    A[size-1, 0] = b
    return A


def jacobi2(iterations, tolerance, size):
    a = 4
    b = -1
    A = tri_diag(a, b, size)
    bs = np.ones(size)
    n = bs.size
    xnews = np.zeros(n)
    kmax = iterations

    for k in range(1, kmax):
        xs = np.copy(xnews)

        for i in range(n):
            slt = A[i,:i]@xs[:i]
            sgt = A[i,i+1:]@xs[i+1:]
            xnews[i] = (bs[i] - slt - sgt)/a

        err = termcrit(xs, xnews)
        if err < tolerance:
            break
    print(xnews)
    print(np.linalg.solve(A, bs))
    return xnews


def jacobi3(iterations, tolerance, size):
    a = 4
    b = -1
    A = tri_diag(a, b, size)
    bs = np.ones(size)
    n = bs.size
    xnews = np.zeros(n)
    kmax = iterations

    for k in range(1, kmax):
        xs = np.copy(xnews)

        for i in range(n):
            slt = A[i,i-1] * xs[i-1] if i > 0 else 0.0
            sgt = A[i,i+1] * xs[i+1] if i < n-1 else 0.0

            if i == n-1:
                slt += A[i, 0] * xs[0]
            elif i == 0:
                sgt += A[0, n-1] * xs[n-1]

            xnews[i] = (bs[i] - slt - sgt)/a

        err = termcrit(xs, xnews)
        if err < tolerance:
            break
    print("jacobi solution:")
    print(xnews)
    print()
    print("np.linalg.solve solution")
    print(np.linalg.solve(A, bs))
    print()
    return xnews


'''
goes to 46th iteration with starting guess
np.array
'''

print("n = 10 \n")
jacobi3(100, 1e-5, 10)

print("n = 20")
jacobi3(100, 1e-5, 20)

'''
increasing size decreases the
difference between
jacobi solution
and
np.linalg.solve solution

jacobi2 is a more general function
which also adds up the zeroes in the
cyclic tridiagonal matrix.

jacobi3 only adds up the nonzero terms.
It does not check all elements or checks
each element and checks if its 0 or not.
'''
