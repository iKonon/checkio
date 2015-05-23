# http://www.circuitstoday.com/half-adder-and-full-adder

'''
To do:
The circuit simulation shown in this chapter works in a backward direction. 
In other words, given a circuit, the output is produced by working back through the input values, 
which in turn cause other outputs to be queried. 
This continues until external input lines are found, at which point the user is asked for values. 
Modify the implementation so that the action is in the forward direction; upon receiving inputs the circuit produces an output.
'''

class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n) # an explicit call to the constructor of the parent class 
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1
        
class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NorGate(OrGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==1 and b==1:
            return 0
        elif (a ==0 and b==1) or (a==1 and b==0):
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    def __init__(self,n):
#        super(LogicGate,self).__init__(n) # a function called super can be used in place of explicitly naming the parent class
        LogicGate.__init__(self,n) # an explicit call to the constructor of the parent class 
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
        
class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1
        
class Connector: # HAS-A LogicGate meaning
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    
class HalfAdder(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a ==1 and b==1:
            SUM = 0
        elif (a ==0 and b==1) or (a==1 and b==0):
            SUM = 1
        else:
            SUM = 0

        if a==1 and b==1:
            CARRY = 1
        else:
            CARRY = 0

        return SUM, CARRY

if __name__ == '__main__':
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())
  
    g5 = NandGate("G5")
    g6 = NorGate("G6")
    g7 = XorGate("G7")
    print(g7.getOutput())
    
    h1 = HalfAdder("H1")
    print(h1.getOutput())