class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        return self.items.append(item)
    
    def  dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
    def size(self):
        return len(self.items)
    
    def display(self):
        if not self.is_empty():
            for _ in self.items:
                print(_, end=' ')
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    
    print("Queue size:", q.size())
    print("Peek:", q.peek())

    print("Dequeue:", q.dequeue())
    print("Queue size after dequeue:", q.size())
    
    print("queue elements: ")
    q.display()
    print()