# Functions in python
A function in its simplest form is just a wrapper name for a block of code. You give it name and then when you call the function by that name, all the code within the function block will be executed. It can help us save time and reduce repeated code.

## Defining a new Function
```
def <function name>():
    print("Hello")
    # Do something else
    # Do something else ...
```
## Calling a Function

Calling a function just means triggering the function. We can call a function at any point in our code in Python.

```
<function name>()
```

### Example :

```
#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function
This code will result in the following sequence of ```
```
output:

Hello
What is your name? #I type sneha
Hello
sneha

```

## Conclusion

Day 06 helped me understand **loops in Python more deeply**, especially the difference between `for` loops and `while` loops. I learned that a `for` loop is generally used when the number of iterations or the sequence to be processed is known, while a `while` loop continues to execute as long as a given condition remains `True`.

By solving different problems on **Reeborg's World**, I was able to apply these concepts practically and understand how loops execute step by step. The exercises helped me improve my logical thinking and made it easier to visualize how `for` and `while` loops work in real programs.

Overall, Day 06 gave me a stronger understanding of **iteration, conditions, and controlling the flow of a program using loops**.


## Reeborg's World Practice

I practiced `for` and `while` loops using different challenges on Reeborg's World.


