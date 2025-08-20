import random

"""
This function uses a nested for loop.
It first loops through i which then loops through j for each i.
i will be the rows so the matrix will be created row by row.
j would be the columns of each row i.
"""


def random_integer_matrix(nrows, ncols):
    mtrx = []

    for i in range(nrows):
        mtrx.append([])
        for j in range(ncols):
            random_num = random.randrange(1, 10)
            mtrx[i].append(random_num)

    return mtrx


"""
This function multiplies each component or index of both 2 lists
and adds it to the integer sum with +=
"""


def scalar_product(list1, list2):
    if len(list1) != len(list2):
        return "Lists must be of the same dimensions."

    sum = 0

    for i in range(len(list1)):
        sum += list1[i] * list2[i]

    return sum


"""
Iterates through the rows then the elements of current row of orig_mtrx.
We set idx = -1 at the start of the iteration of each row.
For each element of the current row, we will append to
the idx-th row, so the rows of the orig_mtrx will
be the new column of the new_mtrx

The try except is to append a new list object or a row if
new_mtrx still does not have it. The except only runs for
the first iteration through rows.
"""


def transpose_matrx(orig_mtrx):
    new_mtrx = []
    for row in orig_mtrx:
        idx = -1

        for element in row:
            idx += 1
            
            try:
                new_mtrx[idx].append(element)
            except:
                new_mtrx.append([])
                new_mtrx[idx].append(element)

    return new_mtrx


"""
Since the rows of left_mtrx must be equal to the
columns of right_mtrx, the number of rows of
left_mtrx or cols of right_mtrx will be the
dimensions of the product of the 2 matrices,
which is n by n.

We use the transpose_matrx function to transpose
the right_mtrx and then take the scalar product
of each rows of left_mtrx and right_mtrx.

Loop through the rows of left_mtrx then
the right_mtrx, multiply the ith row of
left_mtrx to the ith row of the right_mtrx
to get the elements of the ith row of
the new_mtrx

NEEDS A 2D MATRIX AS INPUT SO A VECTOR
(1, 0, 0) is inputted as [[1, 0, 0]]
"""


def matrix_multiply(left_mtrx, right_mtrx):
    new_mtrx = []
    for i in range(len(left_mtrx)):
        new_mtrx.append([])

    new_right_mtrx = transpose_matrx(right_mtrx)

    if len(left_mtrx) != len(new_right_mtrx):
        print("Left matrix must have equal rows as the columns of right matrix.")
        return None

    for i in range(len(left_mtrx)):
        for j in range(len(new_mtrx)):
            new_element = scalar_product(left_mtrx[i], new_right_mtrx[j])
            new_mtrx[i].append(new_element)
    return new_mtrx
