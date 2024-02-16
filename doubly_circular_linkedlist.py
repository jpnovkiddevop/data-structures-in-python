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
            
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.append()
        else:   
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.next.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            
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
print('list before inserting at the beginning')
dcll.display()
dcll.insert_at_beginning(int(input('enter number to append at the beginning  ')))
print('list after appending a node')
dcll.display()       
        