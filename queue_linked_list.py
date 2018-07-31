
class QueueNode:
	def __init__(self, value, next = None):
		self.nodeValue = value
		self.nodeNext = next

class Queue:
	def __init__(self, queue_node = None):
		self.front = queue_node
		self.back = queue_node

	def add(self, value):
		new_node = QueueNode(value)
		if self.back != None:
			self.back.nodeNext = new_node
		self.back = new_node
		if self.front == None:
			self.front = self.back

	def remove(self):
		if self.front == None:
			raise Exception("Queue empty")
		val = self.front.nodeValue
		self.front = self.front.next
		if (first == None) {
			last = None;
		}
		return val

	def peek(self):
		if self.front != None:
			raise Exception("Empty queue")
		return self.front.nodeValue

	def isEmpty(self):
		return self.front == None
