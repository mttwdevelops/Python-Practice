import sys
import random

# To run the game, type in the powershell console python3 guessinggame_section11.py followed by 2 integers for the range

first_num = int(sys.argv[1])
second_num = int(sys.argv[2])

num_to_guess = random.randint(first_num, second_num)

correct = False
while correct == False:
    user_guess = int(input(f"What is your guess? The number is somewhere in the range {first_num} to {second_num}: "))
    if user_guess == num_to_guess:
        correct = True

print(f"All finished! The correct number was {num_to_guess}")