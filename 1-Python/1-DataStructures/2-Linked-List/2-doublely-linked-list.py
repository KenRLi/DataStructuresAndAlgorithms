class Node:
    def __init__(self, value=None, prevNode=None):
        self.value = value
        self.nextNode = None
        self.prevNode = prevNode

    def setValue(self, newVal):
        self.value = newVal

    def getValue(self):
        return self.value

    def setNextNode(self, node):
        self.nextNode = node
    
    def getNextNode(self):
        return self.nextNode

    def setPrevNode(self, node):
        self.prevNode = node
    
    def getPrevNode(self):
        return self.prevNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        if head:
            self.length = 1
        else:
            self.length = 0
    
    def addNode(self, node):
        if (self.length == 0):
            self.head = node
            self.tail = node
        else:
            currTail = self.tail
            currTail.setNextNode(node)
            node.setPrevNode(currTail)
            self.tail = node
        self.length += 1

    def addValue(self, value):
        if (self.length == 0):
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            currTail = self.tail
            node = Node(value, currTail)
            currTail.setNextNode(node)
            self.tail = node
        self.length += 1

    def insertNode(self, index, node):
        if (index == 0):
            nextNode = self.head
            self.head = node
            node.setNextNode(nextNode)
            nextNode.setPrevNode(node)
        elif (index == (self.length - 1)):
            prevNode = self.tail
            self.tail = node
            node.setPrevNode(prevNode)
            prevNode.setNextNode(node)
        else:
            startingNode = None
            numToTraverse = None
            direction = None
            if (index <= (self.length/2)):
                startingNode = self.head
                numToTraverse = index
                direction = +1
            else:
                startingNode = self.tail
                numToTraverse = (self.length - index) - 1
                direction = -1

            
            

        self.length += 1

    def insertVal(self, index, value):


    def removeNode(self, index):
        currNode = self.head
        prevNode = None
        for _ in range(index):
            prevNode = currNode
            currNode = currNode.getNextNode()
        nextNode = currNode.getNextNode()
        prevNode.setNextNode(nextNode)
        nextNode.setPrevNode(prevNode)
        self.length -= 1

    def getNode(self, index):
        currNode = self.head
        for _ in range(index):
            currNode = currNode.getNextNode()
        return currNode

    def getNodeVal(self, index):
        currNode = self.head
        for _ in range(index):
            currNode = currNode.getNextNode()
        return currNode.getValue()

    def setNodeVal(self, index, value):
        currNode = self.head
        for _ in range(index):
            currNode = currNode.getNextNode()
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