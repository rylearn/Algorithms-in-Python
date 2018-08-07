
class Node:
    def __init__(self, key,
                 left = None,
                 right = None,
                 parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def is_internal(self, node):
        if node.left == None and \
            node.right == None:
            return True
        return False

    def insert_node_at_external(self, node, \
                                new_node):
        if self.is_internal(node):
            raise Exception('Not external node')
        if node == None:
            node = new_node
        if new_node.key < node.key:
            node.left = new_node
        else:
            node.right = new_node

    def inorder_traversal(self, node):
        if node != None:
            self.inorder_traversal(node.left)
            print(node.key)
            self.inorder_traversal(node.right)

    def search(self, x, k):
        while x != None or x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while y != None or x == y.right:
            x = y
            y = x.parent
        return y

    def tree_predecessor(self, x):
        if x.left != None:
            return self.maximum(x.left)
        y = x.parent
        while y != None or x == y.left: # test
            x = y
            y = x.parent
        return y

    def tree_insert(self, new_node,\
                    start_node = None):
        if start_node == None:
            start_node = self.root
        x = start_node
        found_node = None
        while x != None:
            found_node = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = found_node
        self.insert_node_at_external(found_node,\
                                     new_node)




