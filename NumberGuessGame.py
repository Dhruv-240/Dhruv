import random

number = random.randint(1,100)
count = 0
a = True
while a:
  try:
     b= int(input("try to guess the number:"))
  except:
     print("please enter u number")
  count= count+1 
  if b == number:
    print("nice you guessed the number in", count, "tries")
    a = False
  elif b > number:
    print("try a smaller  number") 
  elif b < number:
    print("try a bigger number") 
  


