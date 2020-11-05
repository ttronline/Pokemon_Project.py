import random
from time import sleep

choices = ["Charmander","Squirtle","Balbasur"]

computerchoice = random.choice(choices)
print("Computer's Choice is", computerchoice)

player = False

name = input("Hello, Please Enter your Name: ")

while player == False:
    print(f"Hello, {name} Welcome to Pokemon Battle Game")
    player = input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur'\n'Stop the game': 'Stop': Stop: ")

    if player == computerchoice:
        print("\nPlease wait we are loading your results .....")
        sleep(2)
        print("Oh, It's A Tie!!!")
    elif player == "Charmander":
        if computerchoice == "Squirtle":
            print("\nPlease wait we are loading your results .....")
            sleep(2)
            print("Oh, Lost the Game!")
        else:
             print("\nPlease wait we are loading your results .....")
             sleep(2)
             print("Yay, You won the Game!!!!")

    elif player == "Squirtle":
        if computerchoice == "Balbasur":
           print("\nPlease wait we are loading your results .....")
           sleep(2)
           print("Oh, You Lost the Game!!")
        else:
             print("Yay, You won the Game")
    elif player == "Bulbasur":
        if computerchoice == "Charmander":
            print("\nPlease wait we are loading your results .....")
            sleep(2)
            print("You Lost the Game!!!")
        else:
             print("You Won the Game")
    elif player == "Stop":
        print("Thank's For Playing")
        break
    else:
        print("That's not a Valid Play!")


        player = False
