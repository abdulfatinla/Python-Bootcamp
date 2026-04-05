### C8: SETS ##

# A. SETS OPERATION 

fruits = {"apple", "banana", "orange"}
numbers = {1,2,3,4,5}


fruits.add("grape")         # Add element
print(fruits)

fruits.remove("banana")     # Remove element
print(fruits)

fruits.discard("kiwi")      # Remove if exists (no error)
print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {3, 4, 5, 6}

print(set1.union(set2))         # Output: {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # Output: {3, 4}
print(set1.difference(set2))    # Output: {1, 2}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}


grades = [
    ("Alice","Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math",88),
    ("Alice", "English", 95)
]

