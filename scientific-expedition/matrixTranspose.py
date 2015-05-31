'''
In linear algebra, the transpose of a matrix A is another matrix A^T (also written A', A^{tr},t_A or A^t) 
created by any one of the following equivalent actions:

1. reflect A over its main diagonal (which runs from top-left to bottom-right) to obtain A^T
2. write the rows of A as the columns of A^T
3. write the columns of A as the rows of A^T

Formally, the i-th row, j-th column element of A^T is the j-th row, i-th column element of A:
[A^T]_{ij} = [A]_{ji}

If A is an m x n matrix then A^T is an n x m matrix.
You have been given a matrix as a 2D list with integers. Your task is to return a transposed matrix based on input.

Input: A matrix as a list of lists with integers.
Output: The transposed matrix as a list/tuple of lists/tuples with integers.

How it is used: The most obvious use for this idea is in mathematical software, but the concept can be applied in the area of vector graphics. On a computer, one can often avoid explicitly transposing a matrix in memory by simply accessing the same data in a different order.

Precondition:
0 < len(matrix) < 10; all(0 < len(row) < 10 for row in matrix)
'''
def checkio(data):
    return [[x[i] for x in data] for i in range(len(data[0]))]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert isinstance(checkio([[0]]).pop(), list) is True, "Match types"
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"
