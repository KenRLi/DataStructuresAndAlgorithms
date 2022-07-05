class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)
    
    def clear(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

print("Initial stack.")
stack = Stack()
print(stack)

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

for i in range (2):
    retVal = stack.pop()
    print(retVal,"was removed from stack.")
print(stack)