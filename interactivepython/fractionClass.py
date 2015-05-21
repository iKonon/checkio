from __future__ import division

def gcd(m,n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    # http://www.rafekettler.com/magicmethods.html
    def __init__(self,top,bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            if bottom == 0:
                print("NaN")
            else:
                # "lowest terms" representation
                common = gcd(top,bottom)
                self.num = top//common 
                self.den = bottom//common        
        else:
            print("Please enter an integer")

    def getNum(self): # numerator
        return self.num
    
    def getDen(self): # denominator
        return self.den

    def show(self):
        print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden) 
    
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __truediv__(self, otherfraction):
        # from __future__ import division is required
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum,newden)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum
    
if __name__ == '__main__':
    x = Fraction(1,4)
    y = Fraction(1,0)
    z = x + y
''' print(z.getNum())
    print(z.getDen())
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x == y)
    print(x != y)
    print(x < y)
    print(x > y)
'''