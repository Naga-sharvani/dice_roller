from random import randint
import time
import sys


def rolling():
 num: int=randint(1,6)
 return num


print("Press enter to roll the dice")

entered=input("Press any other key to exit ")

while(entered==""):
  n=rolling()
  print("Rolling..")
  for i in range(5,0,-1):
    print(f"{i} ",end="",flush=True)   
    time.sleep(1)
  print("")
  print(f"the number appared on the dice is {n}")
  
  entered=input("Press again..")
  

print("Exiting..")

  