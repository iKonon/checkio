'''
After reading this fragment Nicola wants to build his own "Humpty Dumpty". 
As a basis he chooses the spheroid (read more about it on Wikipedia: http://en.wikipedia.org/wiki/Spheroid). 
We know the height and the width (in inches) for this spheroid. 
For the job at hand, Nikola needs to know how much material is required.

You can help him and create a function to calculate the volume (cubic inches) and the surface area (square inches).

Tips: Be careful with sin-1x -- this is arcsin.

Input: Two arguments. A height and a width as integers.
Output: The volume and the surface area as a list of floats. The results should be accurate to two decimals.

How it is used:
This is a simple math task, but we want to introduce you to the splendid shape -- spheroid (in case you hadn't heard of it yet).
The prolate spheroid is the shape of the ball in several sports, such as in rugby and Australian football. 
In American football, a more pointed prolate spheroid is used. 
Several moons of the Solar system approximate prolate spheroids in shape, though they are actually scalene. 
Examples are Mimas, Enceladus, and Tethys which orbit Saturn and Miranda which orbits Uranus.

The true shape of the Earth is called an Oblate Spheroid, though it is only very slightly oblate. 
The diameter from the North Pole to the South Pole (the shortest diameter) is approximately 12,714 km. 
The equatorial diameter (the longest diameter) is approximately 12,756 km. 
This is not a big difference, but it does mean the Earth is not quite a sphere.

Precondition: 0 < width < 100; 0 < height < 100
'''
from math import pi, asin, atanh, sqrt

def checkio(height, width):
    a = width / 2.0
    c = height / 2.0
    volume = round(pi * 4.0 / 3 * a * a * c, 2)

    if c == a:    # sphere
        surface_area = round(4 * pi * a * a, 2)
    elif c < a:   # oblate spheroid
        e2 = 1 - c * c / a / a
        surface_area = round(2 * pi * a * a * (1 + (1 - e2) / sqrt(e2) * atanh(sqrt(e2))), 2)
    else:         # prolate spheroid
        e2 = 1 - a * a / c / c
        surface_area = round(2 * pi * a * a * (1 + c / a / sqrt(e2) * asin(sqrt(e2))), 2)

    return [volume, surface_area]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"