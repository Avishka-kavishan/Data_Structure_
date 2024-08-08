class Stack :
    def __init__ (self,limit=10):
        self.list = []
        self.limit = limit

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push (self, val):
        return self.list.append(val)
    
    def pop(self):
        if self.list == []:
            return ("Stack is empty")
        else:
            return self.list.pop()
        
    def peek (self):
        if self.list == []:
            return ("stack is empty")
        else:
            return self.list[-1]
        
obj = Stack()
print(obj.isEmpty())

obj.push(5)
obj.push(7)
obj.push(9)
print(obj.peek())
print(obj.list)

obj.pop()

print(obj.list)

    