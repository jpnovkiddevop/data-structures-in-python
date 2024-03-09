
#implementation of Queue data structure using linked list

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
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
    def peek(self):
        return self.front.data
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            removed_node = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return removed_node
        
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current.data, end=' ')
                current = current.next
            print()
            
if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(15)
    
    print(" Queue elements: ")
    q.display()
    
    print("peek element: ", q.peek())
    
    print("dequeued element: ", q.dequeue())
    print("Queue after dequeue:")
    q.display()