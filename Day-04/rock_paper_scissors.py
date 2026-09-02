# Rock-Paper-Scissors Game

import random
game=["rock", "paper", "scissors"]
choice=random.choice(game)
user_choice=input("Enter your choice (rock, paper, scissors): ").lower()
print("Computer chose:", choice)
if(choice=="rock" and user_choice=="scissors"):
    print("You lose! Rock beats scissors.")
elif(choice=="scissors" and user_choice=="paper"):
    print("You lose! Scissors beats paper.")    
elif(choice=="paper" and user_choice=="rock"):
    print("You lose! Paper beats rock.")
elif(choice=="scissors" and user_choice=="rock"):
    print("You win! Rock beats scissors.")
elif(choice=="paper" and user_choice=="scissors"):
    print("You win! Scissors beats paper.") 
elif(choice=="rock" and user_choice=="paper"):
    print("You win! Paper beats rock.")
else:
     print("It's a tie! Both chose", choice)