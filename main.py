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

# Write your code below this line 👇
chart = [rock, paper, scissors]
choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("Did you just typed an invalid number😪, You LOSE, LOOSER.")
    choice = '''
     _             _              
    | |           | |             
  __| | ___  _ __ | | _____ _   _ 
 / _` |/ _ \| '_ \| |/ / _ \ | | |
| (_| | (_) | | | |   <  __/ |_| |
 \__,_|\___/|_| |_|_|\_\___|\__, |
                             __/ |
                            |___/ 
'''
    print(choice)
else:
    print(chart[choice])
    com_choice = random.randint(0, 2)
    print("Computer chose:")
    print(chart[com_choice])

    if choice == com_choice:
        print("It's a Draw")
    elif choice == 0 and com_choice == 2:
        print("You Win!!")
    elif choice == 2 and com_choice == 0:
        print("Computer win!")
    elif choice > com_choice:
        print("You Win!")
    elif com_choice > choice:
        print("Computer Win!!")


# choice = chart[choice]
# print(choice)
# print("Computer chose:")
# com_choice = chart[com_choice]
# print(com_choice)
