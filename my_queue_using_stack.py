"""
enqueue always happen from rear and dequeue from front , FIFO
implementing Queue using stack
Both enqueue and dequeue takes O(1) time.
"""
class  Queue:
    def __init__(self):
        self.stack = []
        
    def  is_empty(self): #check if the queue is empty or not
        return self.stack == []
    
    def enqueue(self, item): #add an element to the rear of the queue
        self.stack.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            removed_item = self.stack.pop(0)
            return removed_item
        else:
            print("Queue is empty")
            
    def peek(self): #return the front of the queue without removing it
        if not self.is_empty():
            return self.stack[0]
        else:
            print("Queue is empty")
    
    def display(self):
        if not self.is_empty():
            for  i in range(len(self.stack)):
                print(self.stack[i],end=" ")
            print()
        else:
            print("Stack is empty")
            
q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(7)

print("Queue elements: ")
q.display()

print("dequeued element is: ", q.dequeue())
print("Queue after the dequeue: ")
q.display()
q.enqueue(9)

print("Queue elements after enqueue: ")
q.display()
