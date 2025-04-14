import random as ran
random = ran.randrange(1,11)
score = 0
user_input = int(input("Guess The Number from 1 to 10: "))
if (random == user_input):
    print("Yes, You dit it.")
    score+=1
else: 
    print(f"Ohh, The number was: {random}")
print(f"Your Current Score is: {score}")