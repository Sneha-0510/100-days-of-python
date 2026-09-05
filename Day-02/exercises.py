# Exercise 1 — Type Checker


name = "Sneha"
age = 19
height = 5.4
is_student = True

print("Data Types:")
print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))
print("Is Student:", type(is_student))



# Exercise 2 — Age in Different Units


age_years = int(input("\nEnter your age in years: "))

age_months = age_years * 12
age_days = age_years * 365

print("Your age in months is approximately:", age_months)
print("Your age in days is approximately:", age_days)


# Exercise 3 — Two Number Calculator


print("\n===== Two Number Calculator =====")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("\nResults:")
print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)

if number2 != 0:
    print("Division:", number1 / number2)
    print("Floor Division:", number1 // number2)
    print("Remainder:", number1 % number2)
else:
    print("Division: Cannot divide by zero.")
    print("Floor Division: Cannot divide by zero.")
    print("Remainder: Cannot divide by zero.")

print("Exponentiation:", number1 ** number2)



# Exercise 4 — Even or Odd


number = int(input("\nEnter an integer: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# Exercise 5 — BMI Calculator


print("\n===== BMI Calculator =====")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))



# Mini Project — Tip Calculator


print("\n===== Tip Calculator =====")

total_bill = float(input("What was the total bill? ₹"))
number_of_people = int(input("How many people are splitting the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))

tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
amount_per_person = final_bill / number_of_people

print("\n===== Bill Summary =====")
print("Original bill: ₹", round(total_bill, 2))
print("Tip amount: ₹", round(tip_amount, 2))
print("Final bill: ₹", round(final_bill, 2))
print("Each person should pay: ₹", round(amount_per_person, 2))



# Number Manipulation Practice


number = 3.14159

print("\nNumber:", number)
print("Rounded number:", round(number))
print("Rounded to 2 decimal places:", round(number, 2))



# Assignment Operators


score = 10

score += 5
print("\nAfter += 5:", score)

score -= 2
print("After -= 2:", score)

score *= 2
print("After *= 2:", score)

score /= 2
print("After /= 2:", score)



# Large Number Readability


population = 1_000_000

print("\nPopulation:", population)


# ============================================================
# End of Day 2
# ============================================================
