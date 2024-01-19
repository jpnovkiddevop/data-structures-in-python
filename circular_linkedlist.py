class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self):
        choices = 1
        while choices:           
            new_node = Node(input("Enter the element to be added at the end of the list "))
            if not self.head:
                self.head = new_node
                new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            choices = int(input("\nDo you want to add more elements? Enter \'1' or any other no to quit "))
    
    def display(self):
        if not self.head:
            print("Circular linked list is empty.")
        current = self.head
        while current.next != self.head:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data)
            

cll = CircularLinkedList()
cll.append()
cll.display()