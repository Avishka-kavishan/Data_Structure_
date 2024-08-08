class Queue:
    def __init__(self):
        self.list = []
    def __str__(self):
        return (self.list)
    
    def isEmpty(self):
        if self.list == []:
            return ("Queue is empty")
        else:
            return ("Queue is not empty")
        
    def enqueue (self, val):
        return self.list.append(val)
    
    def dequeue (self):
        if self.list == []:
            return ("Queue is empty")
        else:
            return self.list.pop(0)
        
    def peek (self):
        if self.list == []:
            return ("Queue is empty")
        else:
            return self.list[0]
        
obj = Queue ()

print(obj.isEmpty())

obj.enqueue(6)
obj.enqueue(7)
obj.enqueue(69)
obj.enqueue(65)
print(obj.list)
obj.dequeue()
print(obj.list)
print(obj.peek())


