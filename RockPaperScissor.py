import random

actions = ["rock", "paper", "scissors"]
while True:
  user = input("Enter your choice rock/ paper/ scissors: ")
  computer = random.choice(actions)
  print("You chose", user, "computer chose", computer)

  
  if user == "rock" or user == "r":
      if computer == "scissors":
          print("Rock smashes scissors! You win!")
      elif computer== "paper":
          print("Paper covers rock! You lose.")
      else:
        print(f"Both players selected {user}. It's a tie!")
  elif user == "paper" or user == "p":
      if computer == "rock":
          print("Paper covers rock! You win!")
      elif computer == "scissors":
          print("Scissors cuts paper! You lose.")
      else:
        print(f"Both players selected {user}. It's a tie!")
  elif user == "scissors" or user == "s":
      if computer == "paper":
          print("Scissors cuts paper! You win!")
      elif computer == "rock":
          print("Rock smashes scissors! You lose.")
      else:
        print(f"Both players selected {user}. It's a tie!")