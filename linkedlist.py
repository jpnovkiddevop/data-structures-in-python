class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        return

    def insert_at_position(self, data, position):
        if position < 0:
            print("invalid position")

        new_node = Node(data)

        current = self.head

        for _ in range(position - 1):
            if current is None:
                print("position out of bounds")
                
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return

    def delete_at_beginning(self):
        if not self.head:
            print("you cant delete from an empty list")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("you cant delete from an empty list")
            return 
        
        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
        return
        
    def delete_at_position(self, position):
        if not self.head:
            print("you cant delete from an empty list")
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(position - 1):
            if current.next:
                current = current.next
            else:
                print("invalid position")
                return
        if current.next:
            current.next = current.next.next
        else:
            print("invalid position")
         
    def reverse_list(self):
        if not self.head or not self.head.next:
            print("you cant reverse a singlular list or an empty list")
            return
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


Linked_List = LinkedList()
Linked_List.insert_at_beggining(5)
Linked_List.insert_at_beggining(8)
Linked_List.insert_at_beggining(9)
Linked_List.insert_at_end(10)
Linked_List.insert_at_position(6, 1)
#Linked_List.delete_at_beginning()
#Linked_List.delete_at_end()
#Linked_List.delete_at_position(1)
Linked_List.display_list()
Linked_List.reverse_list()
print("\nReversed List : \n")
Linked_List.display_list()
