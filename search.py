
import numpy as np
import sys

class Node:
	def __init__(self, value):
		self.value = value
		self.distance = 0
		self.parent_node = None
		self.color = 'white'
		self.f = 0

class Graph:
	def __init__(self, size, value = 0):
		self.nodes = []
		self.number_nodes = size
		for i in range(size):
			self.nodes.append(Node(i))
		
		# map vertex : list of neighboring vertices
		self.adjacency_list = {} 
		for i in range(len(self.nodes)):
			self.adjacency_list[self.nodes[i]] = []

	# nodeA is key
	def addEdge(self, nodeIndex1, nodeIndex2):
		nodeA = self.nodes[nodeIndex1]
		nodeB = self.nodes[nodeIndex2]
		if nodeB not in self.adjacency_list[nodeA]:
			self.adjacency_list[nodeA].append(nodeB)
			self.adjacency_list[nodeB].append(nodeA)

	def getCompleteAdjacentVertices(self):
		return self.adjacency_list

	def getAdjacentVertices(self, vertexV):
		return self.adjacency_list[vertexV]

	def numEdges(self):
		edges = 0
		for i in range(len(self.adjacency_list)):
			for key, list_nodes in self.adjacency_list.items():
				edges += len(list_nodes)
		return edges

	def numNodes(self):
		return len(self.nodes)

	def breadthFirstSearch(self, targetNodeIndex):
		targetNode = self.nodes[targetNodeIndex]
		for node in self.nodes:
			node.color = 'white'
			node.distance = sys.maxint
			node.parent_node = None
		targetNode.color = 'gray' 
		targetNode.distance = 0
		targetNode.parent_node = None
		nodeQueue = []
		nodeQueue.append(targetNode)

		while len(nodeQueue) != 0:
			currentNode = nodeQueue[0]
			del nodeQueue[0]
			for visiting_node in self.adjacency_list[currentNode]:
				if visiting_node.color == 'white':
					visiting_node.color = 'gray'
					visiting_node.distance = currentNode.distance + 1
					visiting_node.parent_node = currentNode
					nodeQueue.append(visiting_node)
			print currentNode.value
			currentNode.color = 'black'

	def depthFirstSearch(self):
		for node in self.adjacency_list:
			node.color = 'white'
			node.parent_node = None
		self.time = 0
		for currentNode in self.nodes:
 			if currentNode.color == 'white':
				self.DFS_Visit(currentNode)

	def DFS_Visit(self, currentNode):
		self.time += 1
		currentNode.color = 'gray'
		currentNode.distance = self.time
		for node in self.adjacency_list[currentNode]:
			if node.color == 'white':
				node.parent_node = currentNode
				node.color = 'gray'
				self.DFS_Visit(node)
		
		currentNode.color = 'black'
		self.time += 1
		currentNode.f = self.time
		print str(currentNode.value) + ' ' + str(currentNode.f)

newG = Graph(4)
newG.addEdge(0, 1)
newG.addEdge(1, 2)
newG.addEdge(1, 3)
newG.breadthFirstSearch(3)
print "DFS: "
newG.depthFirstSearch()


