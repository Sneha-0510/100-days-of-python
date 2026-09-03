# The Random module in Python

The random module is a built-in Python module used when you need to generate random-looking values.

First: Import the module
Before using random, you need to import it.
// import random

## types

### **1. random.random() :**

- `This generates a random decimal number between 0 and 1  i.e;`  
- `0 ≤ number < 1   (number includes 0 but not 1)`
- `also no input taken from users as the lower bound and upper bound is fixed.`
- `can be used to generate random probability `

```<example>
import random
x = random.random()
print(x)
```

<Sample Output>
0.5837291



2. random.randint() :

-It generates a random integer between two numbers.
-random.randint(start, end)
-Both the starting and ending numbers are included.
-start <= number <= end
// rolling a dice

<example>
import random
dice = random.randint(1, 6)
print("You rolled:", dice)

<Sample Output>
You rolled: 4



3. random.randrange() :

-randrange() is similar to randint(), but it behaves like Python's range().
-random.randrange(start, stop)
-the only difference between those two is that
-randint includes both start and end but
-randrange excludes the end

<example>
import random
number = random.randrange(1, 10)
print(number)

<Sample Output>
1 2 3 4 5 6 7 8 9

-you can also provide a step i.e;
-random.randrange(start, stop, step)



4. random.choice() :

-choice() randomly selects one item from a sequence.
// random game character

<example>
import random
characters = ["Warrior", "Mage", "Archer", "Assassin"]
character = random.choice(characters)
print("Your character is:", character)



5. random.choices() :

-choices() can select multiple items.
-random.choices(sequence, k=number)

<example>
import random
colors = ["red", "blue", "green"]
result = random.choices(colors, k=3)
print(result)

-Notice something important:
-Items can repeat.

<Sample Output>
['green', 'green', 'green']

-if you want multiple samples but without repetitions then use random.sample()



6. random.shuffle() :

-shuffle() randomly rearranges a list.

<example>
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

<sample output>
[3, 1, 5, 2, 4]

-shuffle() changes the original list.

7. random.uniform() :

-This generates a random decimal number between two values.
-random.uniform(a, b)

<example>
import random
number = random.uniform(1, 10)
print(number)

<sample output>
4.736281


---------------CHEAT SHEET---------------
RANDOM MODULE
=============

Import:
import random


1. random.random()
   → random float from 0 to <1

2. random.randint(a, b)
   → random integer from a to b
   → both included

3. random.randrange(a, b)
   → random integer from a to b-1
   → b excluded

4. random.choice(sequence)
   → chooses ONE random item

5. random.choices(sequence, k=n)
   → chooses MULTIPLE items
   → repetition allowed

6. random.sample(sequence, k=n)
   → chooses MULTIPLE items
   → no repetition

7. random.shuffle(list)
   → randomly rearranges list
   → changes original list

8. random.uniform(a, b)
   → random float between a and b

9. random.seed(n)
   → makes random sequence reproducible


 #  List in python

 You can create a simple collection of ordered items using a Python list. e.g.

fruits = ["Cherry", "Apple", "Pear"]

or

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

//Accessing Items in Lists
You can provide the name of the list then a square bracket and then the item index that you want. e.g.

states_of_america[0]

will give you "Delaware".

Remember that everything computer related, the first number we count with is 0 and never 1. 0, 1, 2, 3 instead of 1, 2, 3 4.

//Negative Indices
You can access items in the list counting from the end of the list by using negative whole numbers. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #this will be "Pear"
Modifying Items
You can use the same syntax to get hold of items in a List to modify it. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits will now become ["Orange", "Apple", "Pear"]

//Adding Items
You can add items to the end of a List using the append() function. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]