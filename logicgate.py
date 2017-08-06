class InvalidInputError(Exception):
    
    def __init__(self):
        self.message = "INVALID INPUT"

class LogicGate:
    
    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            A = int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
            if A < 0 or A > 1:
                raise InvalidInputError()
            else:
                return A
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            B = int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
            if B < 0 or B > 1:
                raise InvalidInputError()
            else:
                return B
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None
    
    def getPin(self):
        if self.pin == None:
            pin = int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
            if pin < 0 or pin > 1:
                raise InvalidInputError()
            else:
                return pin
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS ON THIS GATE")

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate

class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    def performGateLogic(self):

        pin = self.getPin()
        if (pin < 0 or pin > 1):
            raise InvalidInputError()
        if pin == 0:
            return 1
        else:
            return 0

class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1
class NandGate(BinaryGate):
    
    def performGateLogic(self):
        andG = AndGate("Nand")
        if andG.performGateLogic() == 1:
            return 0
        return 1


class NorGate(BinaryGate):

    def performGateLogic(self):
        orG = OrGate("Nor")
        if orG.performGateLogic() == 1:
            return 0
        return 1

class XorGate(BinaryGate):

    def performGateLogic(self):

        if ((a == 0 and b == 0) or (a == 1 and b == 1)):
            return 0
        else:
            return 1

try:
    a = NandGate("a")
    print(a.performGateLogic())
except InvalidInputError as e:
    print(e.message)

try:
    b = NorGate("b")
    print(b.performGateLogic())
except InvalidInputError as e:
    print(e.message)


c = XorGate("c")
print(c.performGateLogic)