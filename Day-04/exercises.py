import random
#Task 1 — Random number
#Generate a random number between 1 and 100.

choice=random.randrange(1,100)
print("Random number : ",choice)

#Task 2 — Dice
#Simulate rolling a dice.

dice=random.randint(1,6)
print("you rolled : ",dice)

#Task 3 — Coin
#Randomly print either "Heads" or "Tails".

coin=random.choice(["Heads", "Tails"])
print("The coin shows: ",coin)

#Task 4 — Favorite food
#Create a list of 5 foods and randomly choose one.

# method 1
food=["pasta" , "pizza" ,"burger" , "sushi" , "salad"]
choice=random.choice(food)
print("Random food choice: ",choice)

# method 2
food=["pasta" , "pizza" ,"burger" , "sushi" , "salad"]
choice=random.randint(0,len(food)-1)
print("Random food choice: ",food[choice])


#Task 5 — Shuffle
#Create a list of 5 numbers and shuffle them.

items=[1,2,3,4,5]
random.shuffle(items)
print("Shuffled numbers : ",items)

#Task 7 — Lottery
#Create a list of numbers from 1–50 and randomly select 6 different numbers.

lottery_numbers=random.sample(range(1,51),6)
print("Lottery numbers : ",lottery_numbers)

