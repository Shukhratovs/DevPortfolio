import random
from art import logo
from art import vs
from game_data import data
import os

def compare_a(random_index):
  print("Comapre A: " + data[random_index]["name"] + ", " 
        + data[random_index]["description"] + ", from "  
        + data[random_index]["country"] + ".")
  return data[random_index]["follower_count"]

def against_b(random_index):
  print("Against B: " + data[random_index]["name"] + ", " 
        + data[random_index]["description"] + ", from "   
        + data[random_index]["country"] + ".")
  return data[random_index]["follower_count"]

random_index_a = random.randrange(len(data)-1)
random_index_b = random.randrange(len(data)-1)

print(logo)
followers_of_a = compare_a(random_index_a)
print(vs)
followers_of_b = against_b(random_index_b)

is_gameover = True
score_count = 0
score_limit = 0

while is_gameover:
  user_choice = input("Who has more followers? Type 'a' or 'b': ")
  if user_choice == "a" and followers_of_a > followers_of_b:
    score_count += 1
    score_limit += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f"You're right! Current score: {score_count}")
    if score_limit == 2:
      score_limit = 1
      followers_of_a = compare_a(random_index_b)
      print(vs)
      random_index_b = random.randrange(len(data)-1)
      followers_of_b = against_b(random_index_b)
    else:
      followers_of_a = compare_a(random_index_a)
      print(vs)
      random_index_b = random.randrange(len(data)-1)
      followers_of_b = against_b(random_index_b)
    
  elif user_choice == "a" and followers_of_a < followers_of_b:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score_count}")
    is_gameover = False
  if user_choice == "b" and followers_of_b > followers_of_a:
    score_count += 1
    score_limit += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f"You're right! Current score: {score_count}")
    if score_limit == 2:
      score_limit = 1
      followers_of_a = compare_a(random_index_b)
      print(vs)
      random_index_b = random.randrange(len(data)-1)
      followers_of_b = against_b(random_index_b)
    else:
      followers_of_a = compare_a(random_index_b)
      print(vs)
      random_index_b = random.randrange(len(data)-1)
      followers_of_b = against_b(random_index_b)
  elif user_choice == "b" and followers_of_b < followers_of_a:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score_count}")
    is_gameover = False
  