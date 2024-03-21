class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    

    def enqueue_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            new_node.next = new_node  # Circular linking
            new_node.prev = new_node  # Circular linking
        else:
            new_node.next = self.front
            new_node.prev = self.front.prev
            self.front.prev.next = new_node
            self.front.prev = new_node
            self.front = new_node
        self.size += 1


    def enqueue_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            new_node.next = new_node  # Circular linking
            new_node.prev = new_node  # Circular linking
        else:
            new_node.prev = self.rear
            new_node.next = self.rear.next
            self.rear.next.prev = new_node
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

            
    def peek_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("the deque is empty")
            
    def peek_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            print("deque is empty")
            
    def dequeue_front(self):
        if not self.is_empty():
            removed_item = self.front.data
            if self.size == 1:
                self.front = None
                self.rear = None
            else:
                self.front.next.prev = self.rear
                self.front = self.front.next
                self.rear.next = self.front
                
            self.size -= 1
            return removed_item
        else:
            raise IndexError('Deque is empty')
        
    def dequeue_rear(self):
        if not self.is_empty():
            removed_item = self.rear.data
            if self.size == 1 :
                self.rear = None
                self.front = None
            else:
                self.rear.prev.next = self.rear.next
                self.rear = self.rear.prev
                self.front.prev = self.rear
            self.size -= 1
            return removed_item
        
    def get_size(self):
        return self.size
    
    def display(self):
        if not self.is_empty():
            current = self.front
            while current.next != self.front:
                print(current.data, end=' ')
                current = current.next
            print(current.data)
            
q = Deque()
q.enqueue_front(3)
q.enqueue_front(4)
q.enqueue_front(6)
q.enqueue_rear(1)
print("Deque elements: ")
q.display()
print("Size of the deque: ", q.get_size()) 
q.dequeue_front()
print("\nAfter removing front element")
q.display()
q.dequeue_rear()
print("After removing rear element")
q.display()
print("the peek front is: ", q.peek_front())
  