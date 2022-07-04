# Trivial using Lists
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

# Initiallize list
myArray = []

# Add item to end of list
myArray.append("hello")
myArray.append("world")
print(myArray)

# Add item in index position, 0 indexed
myArray.insert(1, "between")
print(myArray)

# Remove first item that matches item, or raises ValueError
myArray.remove("hello")
print(myArray)

# Remove item from end of list (or at index)
x = myArray.pop()
print("Last item in myArray:", x)
print(myArray)

# Populating list with data
for i in range(5):
    myArray.append(i)
print(myArray)

# Remove all items from list
myArray.clear()
print(myArray)

# Built-in list methods
myArray = ['a', 'b', 'c', 'b']
index = myArray.index('b') # Get first index of item
numB = myArray.count('b') # Get number of times item is in list

print(myArray)
print("Index of first 'b': ", index)
print("Number of 'b': ", numB)

myArray.sort() # Sort list
print("Sorted Array:", myArray)

myArray.reverse() # Reverse order of items in list
print(myArray)

newArray = myArray.copy() # Copy (shallow) list to new variable
newArray.pop()

print("Original Array:", myArray)
print("Copied Array:", newArray)