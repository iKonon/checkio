'''
You are given the lengths for each side on a triangle. You need to find all three angles for this triangle. 
If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). 
The angles should be represented as a list of integers in ascending order. 
Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).

Input: The lengths of the sides of a triangle as integers.
Output: Angles of a triangle in degrees as sorted list of integers.

How it is used: This is a classical geometric task. The ideas can be useful in topography and architecture. 
With this concept you can measure an angle without the need for a protractor.

Precondition: 
0 < a,b,c <= 1000
'''

from math import pi, acos

def checkio(a, b, c):
    edges = sorted([a, b, c])
    if edges[0] + edges[1] <= edges[2]:
        return [0, 0, 0]
    
    ang1 = round(acos((edges[1] ** 2 + edges[2] ** 2 - edges[0] ** 2) / float(2 * edges[1] * edges[2]))/pi*180)
    ang2 = round(acos((edges[0] ** 2 + edges[2] ** 2 - edges[1] ** 2) / float(2 * edges[0] * edges[2]))/pi*180)
    ang3 = 180 - ang1 - ang2

    return [ang1, ang2, ang3]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"