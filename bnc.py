# cli-games/bnc.py

greetings = input("Greetings, what is your name? > ")
print("Greetings", greetings)
# cli-games/bnc.py

player = input("Bear, Ninja, or Cowboy? > ")
print(player)
# Import the random library

# Make an array

# Generate a random number to pick a random element from the array
# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

print(computer)
# cli-games/bnc.py

# Compare computer and player role

...
# Replace the print(computer, player) line with the following:
if computer == player:
  print("DRAW!")
else:
  print(computer, player)
  # cli-games/bnc.py

if computer == player:
  print("DRAW!")
elif computer == "Cowboy":
  if player == "Bear":
    print("You lose!", player, "is shot by", computer)
  else: # computer is cowboy, player is ninja
    print("You win!", player, "defeats", computer)
elif computer == "Bear":
  if player == "Cowboy":
    print("You win!", player, "shoots", computer)
  else: # computer is bear, player is ninja
    print("You lose!", player, "is eaten by", computer)
elif computer == "Ninja":
  if player == "Cowboy":
    print("You lose!", player, "is defeated by", computer)
  else: # computer is ninja, player is bear
    print("You win!", player, "eats", computer)
    # cli-games/bnc.py
