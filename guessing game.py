#!/usr/bin/env python
# coding: utf-8

# ### This is going to be a simple guessing game where the computer will generate a random number between 1 to 100, and the user has to guess it in 9 attempts.
# Based on the user's guess, the  computer will give various hints if the number is high or low. When the user guess matches the number computer will print the answer along with the number of attempts. You have to make the submission by uploading your github link to your repositories where you must have pushed your codes.
# 

# In[25]:





import random


no_of_guess = 9
computer_guess = random.randint(1,101)

while no_of_guess > 0:
    user_guess = int(input("Guess a number: "))

    if user_guess == computer_guess:
        print("That is correct, you guessed right!")
        break
        
    elif user_guess < computer_guess:
        print(f"{user_guess} is too low")
        
    elif user_guess > computer_guess:
        print(f"{user_guess} is too high")
        
    no_of_guess -=1 
    print(f"You have {no_of_guess} number of guess left!")
if no_of_guess == 0:
    
    print(f"Sorry, you ran out of guesses. The guess number is {computer_guess}")


# In[ ]:





# In[ ]:





# In[ ]:




