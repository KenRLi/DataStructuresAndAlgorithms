class Queue:
    def __init__(self, max=-1):
        self.queue = []
        self.length = 0
        self.max = max

    def push(self, value):
        if not self.isFull():
            self.queue.append(value)
            self.length += 1
        else:
            print("Cannot push '" + value + "'. Queue is full.")

    def pop(self):
        self.length -= 1
        return self.queue.pop(0)

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
        self.queue = []
        self.length = 0

    def __str__(self):
        return str(self.queue)

print("Initial queue.")
queue = Queue()
print(queue)

if (queue.isEmpty()):
    print("Queue is empty.")

print("Populating queue with values from 0 to 4.")
for i in range(5):
    queue.push(i)
print(queue)

retVal = queue.pop()
print(retVal,"was removed from queue.")
print(queue)

print("Adding 'new' to queue.")
queue.push("New")
print(queue)

queue.setMax(3)

for i in range (2):
    retVal = queue.pop()
    print(retVal,"was removed from queue.")
print(queue)

queue.push("Overflow?")
print(queue)