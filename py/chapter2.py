# A. STRING CREATION
single_quote = 'Hello'
double_quote = "World"
triple_quote = """ I am still new 
and hope I can learn Python and understand it well"""

# ** DOUBLE QUOTE more PREFERRABLE INSTEAD OF SINGLE QUOTE

# B. STRING INDEXING & SLICING
text = "Python Programming"
print(text[0])      # (first character)
print (text[-1])    # (last character)
print (text[0:6])   # (slice 0 to 5)
print (text[:6])    # ( from start to 5)
print (text[7:])    # (7 to end)
print (text[7:16:2]) # (from 7 to 15, every 2 step)


# C. STRING METHODS
name = " bob the builder "

print(len(name))                    # Length, dia kira characters, sekali space front & back
print(name.strip())                 # Remove whitespace, buang front & back spaces, 
                                    # yg tengah punya space bukan whitespace ye.
print(name.upper())                 # Uppercase
print(name.lower())                 # Lowercase
print(name.title())                 # Title case
print(name.replace("bob","jane"))   # Replace

# D. STRING FORMATTING
name = "John Doe"
age = 30

message_1 = f"My name is {name} and I am {age} years old."          # f-strings
message_2 = "My name is {} and I am {} years old.".format(name,age) # str.format()
message_3 = "My name is %s and I am %d years old." % (name,age)     # %-formatting

print(message_1)
print(message_2)
print(message_3)

# E. EXERCISE

text = """ Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This make Python perfect for beginners and experts alike."""

# Answer from ChatGPT
# Count characters (including spaces)
char_count = len(text)

# Count words
words = text.split()
word_count = len(words)

# Count sentences (split by ., !, ?)
import re
sentences = re.split(r'[.!?]+', text)
# Remove empty strings
sentences = [s for s in sentences if s.strip()]
sentence_count = len(sentences)

# Output results
print("Characters:", char_count)
print("Words:", word_count)
print("Sentences:", sentence_count)

# Explanation:
# Characters → len(text) counts everything (including spaces and punctuation).
# Words → split() separates text by spaces.
# Sentences → re.split(r'[.!?]+', text) splits using ., !, or ?.

# re.split() → breaks text into chunks
# [.!?]+ → finds sentence endings
# Extra empty string appears → removed with strip()


# Output:
# Characters: 239
# Words: 38
# Sentences: 5

