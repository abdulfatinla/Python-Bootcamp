#IF ELSE : 2 CONDITION

age = 18

if age>= 18:
    print("You are an adult.")
else:
    print("You are a minor")

# IF -ELIF-ELSE: MORE THAN 2 CONDITIONS

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade >= "F"

print(f"Your grade is: {grade}")

# NESTED CONDITIONS: CONDITION WITHIN CONDITION
weather = "sunny"
temperature = 75

if weather == "sunny":
    if temperature > 70:
        print("It's sunny and warm")
    else:
        print("It's sunny but cool.")


# EXERCISE
weight = float(input("Enter your weight(in Kg): "))
height = float(input("Enter you height(in m): "))
totalbmi = weight/(m^2)



if totalbmi <= 18.5:
   bmi = "Underweight"
elif totalbmi <= 24.9:
    bmi ="Normal Weight"
elif totalbmi <= 29.9:
    bmi = "Overweight"
else:
    bmi ="Obesity"

print = f" Your BMI is:{}"
