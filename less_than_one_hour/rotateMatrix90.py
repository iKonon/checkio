'''
From: https://blog.svpino.com/2015/05/10/programming-challenge-rotating-a-matrix-90-degrees-in-place

Write a function to rotate an NxN matrix by 90 degrees. 
You should rotate it in place, meaning you can't use another matrix to perform the rotation, 
but instead you have to use the same given structure.
'''

def rotateMatrix90(matrix):
    N = len(matrix)
    for ring in range(N//2):
        farthest = N - ring - 1
        for i in range(ring, farthest):
            tmp = matrix[ring][i]
            matrix[ring][i] = matrix[farthest - i + ring][ring]
            matrix[farthest - i + ring][ring] = matrix[farthest][farthest - i + ring]
            matrix[farthest][farthest - i + ring] = matrix[i][farthest]
            matrix[i][farthest] = tmp
    return matrix

if __name__ == '__main__':
    assert rotateMatrix90([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [[13, 9, 5, 1], [14, 10, 6, 2],[15, 11, 7, 3], [16, 12, 8, 4]]