class Node:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def setValue(self, newVal):
        self.value = newVal

    def getValue(self):
        return self.value

    def setNextNode(self, node):
        self.nextNode = node
    
    def getNextNode(self):
        return self.nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        if head:
            self.length = 1
        else:
            self.length = 0
    
    def addNode(self, node):
        if (self.length == 0):
            self.head = node
        else:
            currNode = self.head
            while (currNode.getNextNode() != None):
                currNode = currNode.getNextNode()
            currNode.setNextNode(node)
        self.length += 1

    def addValue(self, value):
        node = Node(value)
        self.addNode(node)

    def insertNode(self, index, node):
        if (index == 0):
            nextNode = self.head
            self.head = node
            node.setNextNode(nextNode)
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.getNextNode()
            nextNode = currNode.getNextNode()
            currNode.setNextNode(node)
            node.setNextNode(nextNode)
        self.length += 1

    def insertVal(self, index, value):
        node = Node(value)
        self.insertNode(index, node)

    def removeNode(self, index):
        currNode = self.head
        prevNode = None
        for _ in range(index):
            prevNode = currNode
            currNode = currNode.getNextNode()
        nextNode = currNode.getNextNode()
        prevNode.setNextNode(nextNode)
        self.length -= 1

    def getNode(self, index):
        currNode = self.head
        for _ in range(index):
            currNode = currNode.getNextNode()
        return currNode

    def getNodeVal(self, index):
        currNode = self.getNode(index)
        return currNode.getValue()

    def setNodeVal(self, index, value):
        currNode = self.getNode(index)
        currNode.setValue(value)

    def __str__(self):
        currNode = self.head

        retStr = "["
        for i in range(self.length):
            val = currNode.getValue()
            if (type(val) is str):
                retStr += '"' + str(currNode.getValue()) + '"'
            else:
                retStr += str(currNode.getValue())
            currNode = currNode.getNextNode()
            if (i != (self.length - 1)):
                retStr += ", "
        retStr += "]"
        return retStr

node1 = Node("hello")
node2 = Node("world")

ll = LinkedList()
print(ll)

ll.addNode(node1)
print(ll)

ll.addNode(node2)
ll.addValue(123)
print(ll)

node3 = Node()
node3.setValue(456)

ll.insertNode(0, node3)
ll.insertVal(2, "third element")
print(ll)

ll.insertVal(0, "first element")
print(ll)

ll.setNodeVal(1, "foo")
ll.setNodeVal(3, "bar")
print(ll)

retNode = ll.getNode(1)
print(retNode.getValue())

retVal = ll.getNodeVal(2)
print(retVal)

ll.removeNode(1)
print(ll)