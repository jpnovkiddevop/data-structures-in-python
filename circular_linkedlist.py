class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self):
        choices = 1
        while choices:           
            new_node = Node(input("Enter the element to be added at the end of the list "))
            if not self.head:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head             
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.tail = new_node
            current.next = new_node
            choices = int(input("\nDo you want to add more elements? Enter \'1' or any other number to quit "))
            
    def delete_at_beginning(self):
        if not self.head:
            print("you cant delete from an empty list")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        self.head = self.head.next
        self.tail.next = self.head
        
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
print("list contains: ")
cll.display()
cll.delete_at_beginning()
print("list after deleting at the beginning: ")
cll.display()
