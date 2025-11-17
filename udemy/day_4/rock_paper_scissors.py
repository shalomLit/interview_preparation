import random

choices_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]
choices_name = ["Rock", "Paper", "Scissors"]

user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_chose not in [0, 1, 2]:
    print("Invalid input! Please choose 0, 1, or 2.")
    exit()

computer_chose = random.randint(0,2)

print(choices_art[user_chose])
print("Computer chose:")
print(choices_art[computer_chose])

if user_chose == computer_chose:
    print("It's a draw")
elif (choices_name[user_chose] == "Rock" and choices_name[computer_chose] == "Scissors" or
      choices_name[user_chose] == "Scissors" and choices_name[computer_chose] == "Paper" or
      choices_name[user_chose] == "Paper" and choices_name[computer_chose] == "Rock"):
    print("You win!")
else:
    print("You lose")

