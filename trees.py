class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):

        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)

        if data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end='')           
            self.inorder_traversal(node.right)

if __name__ == "__main__":

    tree = BinaryTree()
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)

    print("inorder traversal: ")
    tree.inorder_traversal(tree.root)
    print()
