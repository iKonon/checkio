'''
You are given a matrix of NxN (4<=N<=10). You should check if there is a sequence of 4 or more matching digits. 
The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

Input: A matrix as a list of lists with integers.
Output: Whether or not a sequence exists as a boolean.

How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). 
This algorithm can be used for basic pattern recognition.

Precondition:
0 <= len(matrix) <= 10
all(all(0 < x < 10 for x in row) for row in matrix)
'''

def checkio(matrix):
    N = len(matrix)
    def sequence(x, y, dx, dy, diag): # up, down, left, right, diagonals
        if 0 <= x < N and 0 <= y < N and matrix[x][y] == diag:
            return 1 + sequence(x + dx, y + dy, dx, dy, diag)
        else:
            return 0
    
    directions = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if dx != 0 or dy != 0]
    for y in range(N):
        for x in range(N):
            for dx, dy in directions:
                if sequence(x, y, dx, dy, matrix[x][y]) >= 4:
                    return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"