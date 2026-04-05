# LIST 
fruits = ['apple', 'banana', 'orange']
numbers =[1,2,3,4,5]
mixed = ['hello', 42, 3.14, True]
empty_list = []

#Accessing Elements
print(fruits[0])  # Output: 'apple'
print(fruits[-1]) # Output: 'orange'
print(numbers[1:4]) # Output: [2, 3, 4]
print(numbers[:3]) # Output: [1, 2, 3]
print(numbers[2:]) # Output: [3, 4, 5]


fruits.append("grape")    # Add to end
fruits.insert(1, "kiwi")  #  Insert at index
fruits.remove("banana")  # Remove by value
popped = fruits.pop()  # Remove and return last
fruits.sort()  # sort in place
fruits.reverse()    # Reverse in place

print(fruits.append("grape"))
print(fruits.insert(1, "kiwi"))  
print(fruits.remove("banana"))
print(popped = fruits.pop())  
print(fruits.sort()) 
print(fruits.reverse())   


# List operations
len(fruits)             # Length
"apple" in fruits       # Check membership
fruits + ["mango"]      # Concatenation
fruits * 2              # Repetition

print(len(fruits))

