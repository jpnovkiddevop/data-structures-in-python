class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyCircularLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self):
        choices = 1
        while choices:
            new_node =  Node(input("Enter the element to be added at the end of the list "))
     
            if not self.head:
                self.head = new_node
                self.tail = new_node
                self.tail.next = self.head
                self.head.prev = self.tail
                
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
            new_node.next = self.head
            choices = int(input("\nDo you want to add more elements? Enter \'1' or any other number to quit "))
            
    def display(self):
        if not self.head and self.head.next:
            print("you cant display an empty list")
        
        current = self.head
        while current != self.tail:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data)  #print last node
    
dcll = DoublyCircularLinkedlist()
dcll.append()
dcll.display()
        
        