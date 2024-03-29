class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.prev = None
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        return
    
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        if self.head:
            current = self.head
            count = 0
            while count < position - 1 and current.next:
                current = current.next
                count += 1
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            
    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key :
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True#Node/key found and deleted
            current = current.next
        return False #Node/key not found
    
    def reverse(self):
        if not self.head and self.head.next:
            print("you cant reverse an empty or singular list")
            
        current = self.head
        new_head = None
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            new_head = current
            current = next_node
            
        self.head = new_head
            

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = DoublyLinkedList()
x = int(input("enter number to insert at the beginning "))
my_list.insert_at_beginning(x)
num_end = int(input("enter number to insert at end "))
my_list.insert_at_end(num_end)
my_num = int(input("enter number to insert at position "))
position = int(input("enter valid position to insert it "))
num_to_append = int(input("enter number to append "))
my_list.append(num_to_append)
my_list.insert_at_position(my_num, position)
my_list.display_list()
my_list.reverse()
my_list.display_list()