# Trivial using Lists
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

myArray = []

myArray.append("hello") # Add item to end of list
myArray.append("world")

print(myArray)

myArray.insert(1, "between") # Add item in index position

print(myArray)

myArray.remove("hello") # Remove first item that matches item, or raises ValueError

print(myArray)

x = myArray.pop() # Remove item from end of list (or at index)

print("Last item in myArray: ", x)
print(myArray)

for i in range(5):
    myArray.append(i)

print(myArray)

myArray.clear() # Remove all items from list

print(myArray)

myArray = ['a', 'b', 'c', 'b']
index = myArray.index('b') # Get first index of item
numB = myArray.count('b') # Get number of times item is in list

print(myArray)
print("Index of first 'b': ", index)
print("Number of 'b': ", numB)

myArray.sort() # Sort list

print(myArray)

myArray.reverse() # Reverse order of items in list

print(myArray)

newArray = myArray.copy() # Copy (shallow) list to new variable

newArray.pop()

print(myArray)
print(newArray)