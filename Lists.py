class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data

	def getNext(self):
		return self.next

	def setNext(self, nextNode):
		self.next = nextNode

class UnorderedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, data):
		node = Node(data)
		node.setNext(self.head)
		self.head = node
		if self.tail == None:
			self.tail = node

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, data):
		current = self.head
		while current != None:
			if current.getData() == data:
				return True
			current = current.getNext()
		return False

	def remove(self, data):
		current = self.head
		previous = None
		found = False
		while current != None and  not found:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found:
			if previous == None:
				self.head = None
				self.tail = None
			else:
				if self.tail == current:
					self.tail = previous
				previous.next = current.next

	def append(self, data):
		current = self.head
		previous = None
		while current != None:
			previous = current
			current = current.getNext()
		node = Node(data)
		if previous == None:
			self.head = node
		else:
			previous.setNext(node)
		self.tail = node


	def append2(self, data):
		node = Node(data)
		if self.tail == None:
			self.head = node
		else:
			self.tail.setNext(node)
		self.tail = node

class OrderedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, data):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > data:
				stop = True
			else:
				previous = current
				current = current.getNext()
		node = Node(data)
		if previous == None:
			self.head = node
			self.tail = node
		else:
			previous.setNext(node)
			node.setNext(current)
			if self.tail == previous:
				self.tail = node
		

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, data):
		current = self.head
		while current != None:
			if current.getData() == data:
				return True
			else:
				if current.getData() > data:
					return False
			current = current.getNext()
		return False

	def remove(self, data):
		current = self.head
		previous = None
		found = False
		while current != None and  not found:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found:
			if previous == None:
				self.head = None
				self.tail = None
			else:
				if self.tail == current:
					self.tail = previous
				previous.next = current.next

l1 = UnorderedList()
l1.add(3)
l1.add(4)
l1.add(5)
l1.add(2)
l1.add(8)

print(l1.size())

print(l1.search(17))
print(l1.search(8))
l1.remove(5)

print(l1.size())

l1.append(9)
l1.append2(6)

print(l1.size())