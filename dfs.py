
class Node:
	def __init__(self, val):
		self.val = val
		self.visited = False
		self.adj_list = []

	def dfs(self, root):
		if self.root == None:
			return
		self.visit(self.root)
		root.visited = True
		for adj_node in self.adj_list:
			if adj_node.visited == False:
				search(adj_node)

	def bfs(self, root):
		q = Queue()
		root.visited = True
		self.visit(root)
		q.put(root)

		while not q.empty():
			curr_node = q.get()
			for adj_node in curr_node.adj_list:
				if adj_node.visited == False:
					visit(adj_node)
					adj_node.visited = True
					q.put(adj_node)
