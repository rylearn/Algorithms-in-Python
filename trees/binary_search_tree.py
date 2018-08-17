
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

    def tree_insert(self, new_node):
        y = None
        x = self.root
        while x != None:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

    # moving node2 to node1's loc
    def transplant(self, node1, node2):
        # update node1's parent's child
        if node1.parent == None:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2
        # update node2's parent
        if node2 != None:
            node2.parent = node1.parent

    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            # equivalent to :
            # y = self.tree_successor(z)
            y = self.minimum(z.right)
            if y != z.right: ## or y.parent != z
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

root = Node(5)
binary_tree = BinarySearchTree(root)
node = Node(3)
binary_tree.tree_insert(node)
binary_tree.tree_insert(Node(6))
binary_tree.tree_insert(Node(4))
binary_tree.delete(node)
binary_tree.delete(node)
binary_tree.inorder_traversal(binary_tree.root)
