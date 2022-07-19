import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True :
  insert =  int(input(" what do you want to chosose ? type 0 for rock , 1  for paper and  2 for scissors \n"))

  if insert >= 3 or insert <= -1 :
   print("you typed an invalid number , you lose !")
  if insert == 0 :
    print("You chose :")
    print(rock)
  elif insert == 1 :
    print("You cose :")
    print(paper)
  elif insert == 2 :
    print("You chose :")
    print(scissors)


  computer_reply = random.randint(0,2)

  if computer_reply == 0:
    print("computer chose: ")
    print(rock)
  elif computer_reply == 1:
    print("computer chose ")
    print(paper)
  else :
    computer_reply == 2
    print("computer chose :")
    print(scissors)
    # 0 rock 1 paper 2 scicor
  if insert == 0 and  computer_reply == 0 :
    print("its a draw !")
  elif   insert == 1 and  computer_reply == 1 :
    print("its a draw !")
  elif   insert == 2and  computer_reply == 2 :
    print("its a draw !")
  elif   insert == 0 and  computer_reply == 1 :
    print("you lose !")
  elif   insert == 1 and  computer_reply == 2 :
    print("you lose !")
  elif   insert == 2 and  computer_reply == 0 :
    print("you lose !")
  elif   insert == 1 and  computer_reply == 0 :
    print("you win !")
  elif   insert == 2 and  computer_reply == 1 :
    print("you win !")
  elif   insert == 0 and  computer_reply == 2 :
    print("you win !")