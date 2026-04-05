for i in range(5):
    print(i)

for i in range (1,6):
    print(i)

for i in range (0, 10, 2):
    print(i)



# While Loop:

count = 0
while count < 5:
    print (count)
    count += 1


for i in range(10):
    if i==3:
        continue  # Skip this iteration.
    
    if i==7:
        break     # Exit the loop

    print(i)


#### NESTED LOOP ####
for i in range(2):
    for j in range(3):
        print(f"({i}, {j})")


### EXERCISES ###

### 1. EXERCISES CREATE A MULTIPLICATION TABLE GENERATOR ### ###
for i in range(1,13):
    for j in range(1,13):
        print(f"{i} * {j} = {i*j}")

