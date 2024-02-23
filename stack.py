class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

        else:
            print("list is empty")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
            
        else:
            print("list is empty")
            return None
        
    def size(self):
        return len(self.items)
    
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)

print("stack size is: ", stack.size()) #should print 3
print("the top of the stack is: ", stack.peek()) # should print 4

print("popping elements: ")

while not stack.is_empty():
    print(stack.pop())
