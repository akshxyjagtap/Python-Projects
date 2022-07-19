print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride !")
  age = int(input("what is your age ? "))
  if age <= 12 :
      bill = 10
      print("child fare is 10$  ")
      print("photos price is 3$")
      answer = input("do you want photos? 'yes' or 'no' ")
      if  'yes':
        bill +=3
        print(f"your total bill is {bill}$ ")
      elif 'no':
       print(f"your total bill is {bill}$ ")  
  if 12 < age <= 18 :  
    bill=15
    print("youth fare is 15$ ") 
    print("photos price is 3$")
    answer = input("do you want photos? type 'yes' or 'no' ")
    if  'yes':
      bill += 3
      print(f"your total bill is {bill}$ ")
    elif'no':
      print(f"your total bill is {bill}$ ") 

    
  if age>18 :
      print("adult fair is 20$ ")  
      print("photos price is 3$")
      bill=20
      answer = input("do you want photos? 'yes' or 'no' ")
      if  'yes':
       bill+=3
       print(f"your total bill is {bill}$ ") 
      elif 'no':
       print(f"your total bill is {bill}$ ")  
  print('enjoy!')     
else:
 print("sorry can't ride :/")
 print( "come next year ")
   