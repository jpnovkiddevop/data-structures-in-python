"""
circular queue using linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
            
    def dequeue(self):
        if self.is_empty():
            print("the Queue is empty")
        else:
            self.rear.next = self.front.next
            self.front = self.front.next
            
    def peek(self):
        if not self.is_empty():
            return self.front.data
        
    def display(self):
        if  self.is_empty():
            print('The circular queue is Empty')
            
        else:
            current = self.front
            while current.next != self.front:
                print(current.data, end=' ')
                current=current.next
            print(current.data)
            
if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(-2)
    q.enqueue(1)
    
    print("my Queue elements: ")
    q.display()
    print("the list after dequeue", q.dequeue())
    q.display()