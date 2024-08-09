#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("Welcome to the 'Guessing Number' game!")
print("I'm thinking of a number between 1 and 100.")

computer = random.randint(1, 100)
#print(f"Pssst, the correct answer is {computer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")

user_guess = int(input("Make a guess: "))
is_gameover = True
while is_gameover:
    if user_guess > computer:
        attempts -= 1
        print("It's too high")
    elif user_guess < computer:
        attempts -= 1
        print("It's too low")
    elif user_guess == computer:
        print("Congratulations, you got it!")
        is_gameover = False
        break
    if attempts <= 0:
        print("You've run out of attempts! Game Over.")
        is_gameover = False
        break
    print(f"Guess again. You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
