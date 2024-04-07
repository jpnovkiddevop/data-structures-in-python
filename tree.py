class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None        

    def insert_data(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_data(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_data(data)
        else:
            self.data = Node(data)

    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)       

    def preorder_traversal(self, root):
        if root:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)


root = Node(3)
root.insert_data(5)
root.right.insert_data(13)
root.insert_data(6)
root.display()
print("tree elements in inorder traversal: ")
root.inorder_traversal(root)
print("tree elements in preorder: ")
root.preorder_traversal(root)
print("tree elements after postorder traversal: ")
root.postorder_traversal(root)
