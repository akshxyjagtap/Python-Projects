from art import  logo 
from art import  vs
from game_data import data
import random
from replit import clear



score = 0
win = True 
while win == True :
  print(logo)
  

  data 
  # taking random number 
  num_1 = random.randint(0,49)
  num_2 =  random.randint(0,49)
  if num_1 == num_2 :
    num_2 =  random.randint(0,49)


#  extrcting from list and dict
  name_1 = data[num_1]["name" ]
  country_1 = data[num_1]["country"]
  description_1 = data[num_1]["description"]
  follower_1 = data[num_1]["follower_count"]

  name_2 = data[num_2]["name" ]
  country_2 = data[num_2]["country"]
  description_2 = data[num_2]["description"]
  follower_2 = data[num_2]["follower_count"]
  #  printing
  print(f"current score {score}")
  print(f" Compare A: {name_1}  ,country: {country_1} , description : {description_1}")
  print(vs)
  print(f" Against B: {name_2}, country: {country_2} ,description: : {description_2}")
  reply = input("Who has more followers? Type 'A' or 'B'   ").lower()
  if follower_1 > follower_2:
    if reply == "a":
      score +=1
      clear()
      print(f"Thats right current score: {score}")
      
    else  :
      score += 0
      print(f"sorry thats wrong final score {score}")
      win=False

  else :
      if reply == "b":
        score +=1
        clear()
      else  :
        score += 0
        print(f"sorry thats wrong final score {score}")
        win = False
