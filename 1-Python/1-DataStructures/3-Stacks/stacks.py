class Stack:
    def __init__(self, max=-1):
        self.stack = []
        self.length = 0
        self.max = max
    
    def push(self, value):
        if not self.isFull():
            self.stack.append(value)
            self.length += 1
        else:
            print("Cannot push '" + value + "'. Stack is full.")

    def pop(self):
        self.length -= 1
        return self.stack.pop()

    def setMax(self, max):
        self.max = max

    def getLength(self):
        return self.length

    def isEmpty(self):
        return self.length == 0
    
    def isFull(self):
        if (self.max == -1):
            return False
        return self.length == self.max
    
    def clear(self):
        self.stack = []
        self.length = 0

    def __str__(self):
        return str(self.stack)

print("Initial stack.")
stack = Stack()
print(stack)

if (stack.isEmpty()):
    print("Stack is empty.")

print("Populating stack with values from 0 to 4.")
for i in range(5):
    stack.push(i)
print(stack)

retVal = stack.pop()
print(retVal,"was removed from stack.")
print(stack)

print("Adding 'new' to stack.")
stack.push("New")
print(stack)

stack.setMax(3)

for i in range (2):
    retVal = stack.pop()
    print(retVal,"was removed from stack.")
print(stack)

stack.push("Overflow?")
print(stack)