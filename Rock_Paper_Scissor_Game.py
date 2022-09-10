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

#Write your code below this line 👇
user = int(input("Choose:-\n 1.for Stone \n 2.for Paper \n 3.for Scissor\n"))
while(user<=3 and user>0):

  computer = random.randint(1,3)
  if user == 3 and computer == 2:
    print("You Choose:\n")
    print(scissors)
    print("Computer Choose:\n")
    print(paper)
    print("You are Winner!")
    break
  elif user == 3 and computer == 1:
    print("You Choose:\n")
    print(scissors)
    print("Computer Choose:\n")
    print(rock)
    print("Computer Winner!")
    break
  elif user == 3 and computer == 3:
    print("You Choose:\n")
    print(scissors)
    print("Computer Choose:\n")
    print(scissors)
    print("It's a draw!")
    break
  elif user == 1 and computer == 2:
    print("You Choose:\n")
    print(rock)
    print("Computer Choose:\n")
    print(paper)
    print("Computer Winner!")
    break
  elif user == 1 and computer == 3:
    print("You Choose:\n")
    print(rock)
    print("Computer Choose:\n")
    print(scissors)
    print("You are Winner!")
    break
  elif user == 1 and computer == 1:
    print("You Choose:\n")
    print(rock)
    print("Computer Choose:\n")
    print(rock)
    print("It's a draw!")
    break
  elif user == 2 and computer == 1:
    print("You Choose:\n")
    print(paper)
    print("Computer Choose:\n")
    print(rock)
    print("You are Winner!")
    break
  elif user == 2 and computer == 3:
    print("You Choose:\n")
    print(paper)
    print("Computer Choose:\n")
    print(scissors)
    print("Computer Winner!")
    break
  else:
    print("You Choose:\n")
    print(paper)
    print("Computer Choose:\n")
    print(paper)
    print("It's a draw!")
    break
print("You choose a wrong number")
