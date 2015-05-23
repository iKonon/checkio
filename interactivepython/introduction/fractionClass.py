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
        if bottom == 0:
            raise ValueError("Division by zero")
        else:
            if isinstance(top, int) and isinstance(bottom, int):
                # "lowest terms" representation
                common = gcd(top,bottom)
                self.num = top//common 
                self.den = bottom//common        
            else:
                raise ValueError("Please enter an integer for a numerator and a denominator.")
   
    def __new__(self,top,bottom):
        if bottom == 0:
            raise ValueError("Division by zero")
        else:
            return super(Fraction,self).__new__(self,top,bottom)
            
    def getNum(self): # numerator
        return self.num
    
    def getDen(self): # denominator
        return self.den

    def show(self):
        print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden) 

    def __radd__(self,otherfraction):
        return self.__add__(otherfraction) 
    
    def __iadd__(self,otherfraction):
        return self.__add__(otherfraction) 
    
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
    x = Fraction(2,3)
    y = Fraction(1,2)
    z = x + y
    print("x is %s, y is %s, z = x+y" % (x,y))
    print("Numerator of z is %s" % z.getNum())
    print("Denominator of z is %s" %z.getDen())
    print(x,y,z) # __repr__
    x += y
    print("x is %s, y is %s" % (x,y))   
    print("x + y equals %s" % (x+y))
    print("y + x equals %s" % (y+x))
    print("x - y equals %s" % (x-y))
    print("x * y equals %s" % (x*y))
    print("x / y equals %s" % (x/y))
    print("x == y: %s" % (x == y))
    print("x != y: %s" % (x != y))
    print("x < y: %s" % (x < y))
    print("x > y: %s" % (x > y))
