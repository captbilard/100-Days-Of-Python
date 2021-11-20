from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(
    input("What do you choose? Type 0 for 'Rock', 1 for 'paper', 2 for 'scissors'? \n")
)
computer_choice = randint(0, 2)

if user_choice > 2 or user_choice < 0:
    print("You've chosen an invalid number, you lose")
    quit()

dict = {0: rock, 1: paper, 2: scissors}

win_message = "You win"
lose_message = "You lost"

print(dict[user_choice] + "\n")
print("Computer chose:\n")
print(dict[computer_choice] + "\n")



def check_game(val1, val2):
    val1, val2 = dict[val1], dict[val2]
    if val1 == rock and val2 == scissors:
        return True
    elif val1 == scissors and val2 == paper:
        return True
    elif val1 == paper and val2 == rock:
        return True


if user_choice == computer_choice:
    print("Draw")
elif check_game(user_choice, computer_choice) == True:
    print(win_message)
else:
    print(lose_message)
