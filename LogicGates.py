class LogicGate():
	def __init__(self, label):
		self.label = label

	def getOutput(self):
		return self.performGateLogic()

	def getLabel(self):
		return self.label

class BinaryGate(LogicGate):
	def __init__(self, label):
		LogicGate.__init__(self, label)

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter value for pin A for gate "+self.getLabel()+" >>"))
		else:
			return self.pinA.getFrom().getOutput()
	
	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter value for pin B for gate "+self.getLabel()+" >>"))
		else:
			return self.pinB.getFrom().getOutput()

	def setPin(self, conn):
		if self.pinA == None:
			self.pinA = conn
		else:
			if self.pinB == None:
				self.pinB = conn
			else:
				print("No free pins")

class UnaryGate(LogicGate):
	def __init__(self, label):
		LogicGate.__init__(self, label)

		self.pin = None

	def getPin(self):
		if self.pin == None:
			return int(input("Enter value for pin for gate "+self.getLabel()+" >>"))
		else:
			return self.pin.getFrom().getOutput()

	def setPin(self, conn):
		if self.pin == None:
			self.pin = conn
		else:
			print("No free pins")

class ORGate(BinaryGate):
	def __init__(self, label):
		BinaryGate.__init__(self, label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 | b == 1:
			return 1
		else:
			return 0

class NOTGate(UnaryGate):
	def __init__(self, label):
		UnaryGate.__init__(self, label)

	def performGateLogic(self):
		a = self.getPin()
		if a == 0:
			return 1
		else:
			return 0

class ANDGate(BinaryGate):
	def __init__(self, label):
		BinaryGate.__init__(self, label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 & b == 1:
			return 1
		else:
			return 0

class NORGate(BinaryGate):
	def __init__(self, label):
		BinaryGate.__init__(self, label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 | b == 1:
			return 0
		else:
			return 1

class NANDGate(BinaryGate):
	def __init__(self, label):
		BinaryGate.__init__(self, label)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 & b == 1:
			return 0
		else:
			return 1

class Connector():
	def __init__(self, gate1, gate2):
		self.gfrom = gate1
		self.gto = gate2

		gate2.setPin(self) 

	def getFrom(self):
		return self.gfrom

g1 = ANDGate("AB")
g2 = ANDGate("CD")
g3 = NORGate("N")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
print(g3.getOutput())