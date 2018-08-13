
class StackNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class Stack:
	def __init__(self, top_value):
		self.stack_top = StackNode(top_value)

	def pop(self):
		if self.stack_top == None:
			raise Exception("Stack empty")
		ret_val = self.stack_top.value
		self.stack_top = self.stack_top.next
		return ret_val

	def push(self, value):
		new_node = StackNode(value)
		new_node.next = self.stack_top
		self.stack_top = new_node

	def peek(self):
		if self.stack_top == None:
			raise Exception("Stack empty")
		return self.stack_top.value

	def empty(self):
		return self.stack_top == None

new_stack = Stack(5)
new_stack.push(5)
new_stack.push(7)
print new_stack.pop()
print new_stack.peek()
print new_stack.pop()
print new_stack.pop()
new_stack.push(6)
print new_stack.pop()