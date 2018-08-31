
class Queue:

	def __init__(self):
		self.arr = []

	# adds item to queue
	def add(self, item):
		self.arr.reverse()
		self.arr.append(item)
		self.arr.reverse()

	# remove first item from queue
	def remove(self):
		if self.isEmpty():
			return None

		self.arr = self.arr[1:]

		if self.isEmpty():
			return None
		return self.arr[0]

	def peek(self):
		if self.isEmpty():
			return None
		return self.arr[0]

	def isEmpty(self):
		return len(self.arr) == 0

airport_line = Queue()
airport_line.add("jeff")
airport_line.add("stan")
print airport_line.peek()
print airport_line.isEmpty()
airport_line.remove()
print airport_line.peek()
airport_line.remove()
print airport_line.peek()
print airport_line.isEmpty()
