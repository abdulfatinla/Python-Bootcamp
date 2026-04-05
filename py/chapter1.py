name = "Fatin"      # String
age = 33            # Integer
weight = 78.56      # Float
is_female = False   # Boolean

print(name)
print(type(name))

print(age)
print(type(age))

print(weight)
print(type(weight))

print(is_female)
print(type(is_female))

# MATH OPERATIONS
x = 10
y = 2

print(x + y)    # Addition
print(x - y)    # Subtraction
print(x * y)    # Multiplication
print(x / y)    # Division
print(x // y)   # Floor Division
print(x % y)    # Modulus # baki(remainder) selepas bahagi
                         # utk nak check genap cth baki 0/ganjil cth baki 1
                         # 8 % 2 = 0 → sebab 8 bahagi 2 tiada baki
                         # 7 % 4 = 3 → sebab 7 ÷ 4 = 1 baki 3
                         # 15 % 6 = 3 → sebab 15 ÷ 6 = 2 baki 3       
print(x ** y)   # Exponentation 
                        # 5^2 = 25 → 5 × 5
                        # 3^4 = 81 → 3 × 3 × 3 × 3
                        # 7^0 =1 (any number to power 0 equals 1)

# Exercise - Convert Celsius to Fahrenheit
C = 25
F = (C *9/5 + 32)
print(F)
