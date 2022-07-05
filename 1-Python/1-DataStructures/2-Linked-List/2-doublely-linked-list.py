class Node:
    def __init__(self, value=None, prevNode=None, nextNode=None):
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

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
    def __init__(self, initNode=None):
        self.head = initNode
        self.tail = initNode
        if initNode:
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
        node = Node(value)
        self.addNode(node)

    def insertNode(self, index, node):
        if (index == 0):
            nextNode = self.head
            nextNode.setPrevNode(node)
            node.setNextNode(nextNode)
            self.head = node
        elif (index == (self.length - 1)):
            prevNode = self.tail
            prevNode.setNextNode(node)
            node.setPrevNode(prevNode)
            self.tail = node
        else:
            if (index <= (self.length/2)):
                currNode = self.head
                numToTraverse = index - 1
                direction = +1
            else:
                currNode = self.tail
                numToTraverse = (self.length - index) - 1
                direction = -1

            for _ in range(numToTraverse):
                if (direction > 0):
                    currNode = currNode.getNextNode()
                else:
                    currNode = currNode.getPrevNode()

            if (direction > 0):
                nextNode = currNode.getNextNode()
                currNode.setNextNode(node)
                nextNode.setPrevNode(node)
                node.setPrevNode(currNode)
                node.setNextNode(nextNode)
            else:
                nodeBefore = currNode.getPrevNode()
                currNode.setPrevNode(node)
                nodeBefore.setNextNode(node)
                node.setPrevNode(nodeBefore)
                node.setNextNode(currNode)
        self.length += 1

    def insertVal(self, index, value):
        node = Node(value)
        self.insertNode(index, node)

    def removeNode(self, index):
        if (index <= (self.length/2)):
            currNode = self.head
            numToTraverse = index
            direction = +1
        else:
            currNode = self.tail
            numToTraverse = (self.length - index)
            direction = -1

        for _ in range(numToTraverse):
            prevNode = currNode
            if (direction > 0):
                currNode = currNode.getNextNode()
            else:
                currNode = currNode.getPrevNode()
        
        if (direction > 0):
            nextNode = currNode.getNextNode()
            prevNode.setNextNode(nextNode)
            nextNode.setPrevNode(prevNode)
        else:
            nodeBefore = currNode.getPrevNode()
            prevNode.setPrevNode(nodeBefore)
            nodeBefore.setNextNode(prevNode)

        self.length -= 1

    def getNode(self, index):
        if (index <= (self.length/2)):
            currNode = self.head
            numToTraverse = index
            direction = +1
        else:
            currNode = self.tail
            numToTraverse = (self.length - index)
            direction = -1

        for _ in range(numToTraverse):
            if (direction > 0):
                currNode = currNode.getNextNode()
            else:
                currNode = currNode.getPrevNode()
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