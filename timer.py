import time

def countdown(t):

  while t:
    print(t)
    time.sleep(1)
    t -= 1
  print("time's up")



t = input("Enter the time in seconds: ")
countdown(int(t))