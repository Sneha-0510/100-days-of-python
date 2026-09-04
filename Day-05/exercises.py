#codes I practised today


#Predict what will be printed from the code below:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


# Finding the sum of all numbers in  a list

li=[101,23,43,45,64,65,87,90,100]
sum=0
for i in range(len(li)):
    sum+=li[i]  
print("The sum of all numbers in the list is:",sum)


# Finding the largest number in a list

li=[101,23,43,45,64,65,87,90,100]
score=0
for i in li:
    if i>score:
        score=i
print("The largest number in the list is:",score)


# The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

sum=0
for i in range(1,101):
    sum+=i  
print("The sum of all numbers in the list is:",sum)