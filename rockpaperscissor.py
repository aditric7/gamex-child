#py rock paper scissor game 
import random
#gaming rules is that if user selects 
#rock vs paper -> paper wins 
#scissor vs rock -> rock wins
#paper  vs scissor -> scissor wins
while True:
  print("user selects any 1 option :")
  print("Option 1 -> Rock")
  print("Option 2 -> Scissor")
  print("Option 3 -> Paper")

  user=int(input("Choose any option from (1-3)\n"))
  computer=random.randint(1,3)

  if user==1:
    print("user chose Rock")
  elif user==2:
    print("user chose Scissor")
  else:
   print("user chose Paper")

  if computer==1:
    print("chose Rock")
  elif computer==2:
    print("chose Scissor")
  else:
    print("chose Paper")

  if user==computer:
    print("It's a Draw ")
  elif user==1 and computer==3:
    print("computer wins!")
  elif user==2 and computer==1:
    print("computer wins!")
  elif user==3 and computer==2:
    print("computer wins!")
  else :
    print("user wins!!")
  again=input("Play again ? (yes/no):\n")
  if again =="no":
    break
print("Thanks for playing!!")