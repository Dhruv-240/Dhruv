import random
import time

roll_again = "yes"



while roll_again == "yes" or roll_again == "y":

  print("rolling")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("The values is :", random.randint(1,6))
  time.sleep(1)

  roll_again = input("Roll the Dices Again?")