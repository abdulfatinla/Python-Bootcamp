#### CHAPTER 1 : VARIABLE & DATA TYPE
General Notes
# In Terminal
1. Create virtual environment (venv), is to to isolate project dependencies and prevent conflicts with other projects or your system's global Python installation.

2. Create (venv) >> 
python -m venv myvenv

3. Activate (venv)>> 
myvenv\Scripts\activate

4. Command Python in new terminal >>
cd py  

5. Run python file in terminal >> py yourfilename.py
contoh : py chapter1.py

 6. Please save dulu at the coding tab, if not save, cannot run at terminal.
Click ctrl+s  at the tab to save 

# VARIABLE
def: name assigend to particular data
cth:
a = 1
b = 3
job = waiter

# DATA TYPE
1. String           >> " "/' '/""" """
2. Integer number   >> 2
3. Float            >> 3.5
4. Boolean          >> True / False

Contoh:
name = "Fatin"      # String
age = 33            # Integer
weight = 78.56      # Float
is_female = False   # Boolean

# PRINT
1. Print the message or results on a screen
print ()

2. Determine Type of Data
print (type(variable))
contoh :
b = 16
print (type(b))

Jawapan: Int 
 
# MATH OPERATIONS
x = 10
y = 2

print(x + y)    # Addition
print(x - y)    # Subtraction
print(x * y)    # Multiplication
print(x / y)    # Division
print(x // y)   # Floor Division
print(x % y)    # Modulus
print(x ** y)   # Exponentiation


# Exercise - Convert Celsius to Fahrenheit
C = 25
F = (C *9/5 + 32)
print(F)

### CHAPTER 2 : STRING MANIPULATION
# STRING MANIPULATION
# A. STRING CREATION
1. Single Quote (one liner)
2. Double Quote (one Liner)
3. Triple Quote (Multiliner)

single_quote = 'Hello'
double_quote = "World"
triple_quote = """ I am still new 
and hope I can learn Python and understand it well"""

***** ZAROL SAID, PLEASE USE DOUBLE QUOTE INSTEAD OF SINGLE QUOTE

# B. STRING INDEXING & SLICING
text = "Python Programming"
print(text[0])      # (first character)
print (text[-1])    # (last character)
print (text[0:6])   # (slice 0 to 5)
print (text[:6])    # ( from start to 5)
print (text[7:])    # (7 to end)
print (text[7:16:2]) # (from 7 to 15, every 2 step)

jawapan:
P
g
Python
Python
Programming
Pormi
17

# C. STRING METHODS
name = " bob the builder "

print(len(name))                    # Length, dia kira characters, sekali space front & back
print(name.strip())                 # Remove whitespace, buang front & back spaces, 
                                    # yg tengah punya space bukan whitespace ye.
print(name.upper())                 # Uppercase
print(name.lower())                 # Lowercase
print(name.title())                 # Title case
print(name.replace("bob","jane"))   # Replace

jawapan:
17
bob the builder
 BOB THE BUILDER
 bob the builder
 Bob The Builder
 jane the builder

# D. STRING FORMATTING
name = "John Doe"
age = 30

message_1 = f"My name is {name} and I am {age} years old."          # f-strings
message_2 = "My name is {} and I am {} years old.".format(name,age) # str.format()
message_3 = "My name is %s and I am %d years old." % (name,age)     # %-formatting

print(message_1)
print(message_2)
print(message_3)

jawapan:
My name is John Doe and I am 30 years old.
My name is John Doe and I am 30 years old.
My name is John Doe and I am 30 years old.

