class Node:
    def __init__ (self,data):
        self.data = data
        self.nextNode = None

class Stack :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push (self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.nextNode = newNode
            self.tail = newNode

        self.length += 1

    def pop (self):
        if self.head is None:
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.nextNode
        return popped_node.data

    def display (self):
        if self.head is None:
            print("None")
            return
        
        currentNode = self.head
        stack_elements = []
        while currentNode:
            stack_elements.append(currentNode.data)
            currentNode = currentNode.nextNode
        return stack_elements



obj = Stack()
print(obj.display())

obj.push(12)
obj.push(22)
obj.push(32)
obj.push(42)

print(obj.display())
obj.pop()
print(obj.display())




