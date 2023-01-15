# Rock-Paper-Scissors Game
import random
print("Welcome to Rock-Paper-scissors Game")

# ASCII ART
print('⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀             ⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀ ⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              ⡼⠋⠀⠀⠀ ⢀⡿⠀⠀⠀⠀⠀⠀⠀\n'
      '⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀ ⠘⢧⠈⢿⡀         ⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀ ⣴⠟⠁⠀⠀⠀ ⣰⠏⠀ ⢀⣤⣤⣄⡀⠀⠀\n'
      '⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠟⠛⠛⠃⠸⡇        ⠈⣇⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀   ⠈⠹⡆⠀\n'
      '⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀  ⢠⣤⡤⠶⠖⠛⠀⣿⠀        ⣿⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀   ⢀⣠⡾⠃⠀\n'
      '⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣠⡤⠖⠋⢀⣿      ⣠⠏⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀    ⣠⠶⠋⠁⠀⠀⠀\n'
      '⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣠⡾⠋⠁⠀⠀  ⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀        ⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄\n'
      '⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀  ⢀⣠⠾⠋⠀⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀          ⢀⣠⠼⠃\n'
      '⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀          ⣀⣤⠶⠛⠉⠀⠀⠀\n'
      '⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀      ⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀    ⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
      '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

print("Let's Begin!")

# ASCII ART
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

# User's Choice
print("Type 0 for Rock \nType 1 for Paper \nType 2 for Scissors\n")
user_choice = int(input("what is your choice?\n"))

# Choice List
game_images = [rock, paper, scissors]

# Statement
if user_choice >= 3 or user_choice < 0:
    print("Invalid number, Choose only between 0 to 2")
else:
    choice_1 = game_images[user_choice]
    print(choice_1)

# Computer choice
    print("Computer choice:")
    computer_choice = random.randint(0, 2)
    choice_2 = game_images[computer_choice]
    print(choice_2)

    if computer_choice == 2 and user_choice == 0:
          print("HURRAY! You won")
    elif computer_choice < user_choice:
          print("HURRAY! You won")
    elif computer_choice == 0 and user_choice == 2:
          print("you lose!")
    elif user_choice < computer_choice:
          print("You lose!")
    elif computer_choice == user_choice:
          print("It's a draw!")

print("\nHave Fun!")










