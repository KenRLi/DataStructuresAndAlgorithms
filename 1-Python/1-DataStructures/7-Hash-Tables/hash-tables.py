# Trivial using Dictionaries
# https://www.w3schools.com/python/python_dictionaries.asp

import random

class HashTable:
    def __init__(self, tableSize):
        self.hashTable = {}
        self.tableSize = tableSize

    def hash(self, value):
        intVal = int(value)
        return intVal % self.tableSize

    def add(self, value):
        hashKey = self.hash(value)
        if (hashKey in self.hashTable):
            self.hashTable[hashKey].append(value)
        else:
            self.hashTable[hashKey] = [value]

    def getHashTable(self):
        return self.hashTable

itemsToHash = []
for _ in range(25):
    itemsToHash.append(random.randint(1,1000))
print(itemsToHash)

hashtable = HashTable(9)

for item in itemsToHash:
    hashtable.add(item)

print(hashtable.getHashTable())