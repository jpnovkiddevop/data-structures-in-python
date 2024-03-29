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
            self.tail.next = new_node
            self.head = new_node
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head.next == self.tail:
            new_node.next = self.tail.next
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next != self.tail.next:
                current = current.next
            new_node.next = self.tail.next
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
            

    def insert_at_position(self, data, pos):
        new_node = Node(data)  # Creating a new node with the provided data

        # If the list is empty or the position is 0, append to the beginning of the list
        if not self.head or pos <= 0:
            self.append(data)
        else:
            current = self.head
            # Traverse the list until the position or the end of the list is reached
            for _ in range(pos - 1):
                if current.next:
                    current = current.next
                else:
                    print("position out of range")
                    break  # Break if the end of the list is reached before the desired position

            # Insert the new node after the current node
            next_node = current.next
            current.next = new_node

            # Update pointers for the new node
            new_node.next = next_node
            if next_node:
                next_node.prev = new_node
            new_node.prev = current

            # Update the tail node if the new node is inserted at the end
            if not next_node:
                self.tail = new_node
                
    def delete_at_beginning(self):
        if not self.head:
            print('you cant delete from an empty list')
            
        next_node = self.head.next
        next_node.prev = self.tail.next
        self.tail.next = next_node
        self.head = next_node
        

    def delete_at_end(self):
        if not self.head:
            raise Exception('Cannot delete from an empty list')

        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.prev.next = self.head
        self.head.prev = current.prev
        
    def delete_at_end(self):
        if not self.head:
            raise Exception('Cannot delete from an empty list')

        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.prev.next = self.head
        self.head.prev = current.prev

    def display(self):
        if not self.head:
            print("The list is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break


    
dcll = DoublyCircularLinkedlist()
dcll.append()
print('list before inserting at the beginning')
dcll.display()
print()
dcll.insert_at_beginning(int(input('enter number to append at the beginning  ')))
print('list after appending a node')
dcll.display()       
print('list after inserting at the end')
dcll.insert_at_end(9)  
dcll.display()     
print('list after inserting at specified position')
dcll.insert_at_position(5, 3)
dcll.display() 
print('list after deleting first element')
dcll.delete_at_beginning()
dcll.display()
print('list after deleteing data at end')
dcll.delete_at_end()
dcll.display()
