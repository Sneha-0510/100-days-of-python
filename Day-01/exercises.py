# Exercise 1 — Personal Information


name = "Sneha"
age = 19
branch = "AI & DS"
college = "CMRIT"

print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("College:", college)



# Exercise 2 — Greeting Program


name = input("What is your name? ")

print("Hello " + name + "!")



# Exercise 3 — Age Calculator


age = int(input("Enter your age: "))

next_year_age = age + 1

print("Next year you will be", next_year_age, "years old.")



# Exercise 4 — String Length


name = input("Enter your name: ")

name_length = len(name)

print("Your name has", name_length, "characters.")



# Exercise 5 — Simple Calculator


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print("\nResults:")
print("Sum:", addition)
print("Difference:", subtraction)
print("Product:", multiplication)

if second_number != 0:
    division = first_number / second_number
    print("Division:", division)
else:
    print("Division: Cannot divide by zero.")


# Exercise 6 — Data Types


student_name = "Sneha"
student_age = 19
student_height = 5.4
is_student = True

print("\nData Types:")
print("student_name:", type(student_name))
print("student_age:", type(student_age))
print("student_height:", type(student_height))
print("is_student:", type(is_student))



# Exercise 7 — Type Conversion


number_as_string = "25"

number_as_integer = int(number_as_string)

print("\nType Conversion:")
print("Original value:", number_as_string)
print("Converted value:", number_as_integer)
print("Original type:", type(number_as_string))
print("Converted type:", type(number_as_integer))



# Mini Project — Student Introduction Generator


print("\n===== Student Introduction Generator =====")

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_branch = input("Enter your branch: ")
student_college = input("Enter your college: ")
student_city = input("Enter your city: ")

print("\n===== Introduction =====")
print("Hello! My name is " + student_name + ".")
print(
    "I am",
    student_age,
    "years old and I study",
    student_branch,
    "at",
    student_college + "."
)
print("I am from", student_city + ".")


# ============================================================
# End of Day 1
# ============================================================