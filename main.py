from random import randint
from time import sleep
from ast import literal_eval
from os.path import isfile

if isfile("./data"):
    with open('data', 'r') as f:
        data = literal_eval(f.read())  # writes to data as list, not string
else:
    data = {'wins': 0, 'loses': 0, 'draws': 0}
    with open("data", "w+") as f:
        f.write("{'wins': 0, 'loses': 0, 'draws': 0}")


def main():
    while True:
        player = input("Choose Rock, Paper or Scissors:").lower()
        if player == "rock" or player == "r":
            print("You have chosen Rock")
            player = 1
            break
        elif player == "paper" or player == "p":
            print("You have chosen Paper")
            player = 2
            break
        elif player == "scissors" or player == "s":
            print("You have chosen Scissors")
            player = 3
            break
        else:
            print("Error: Incorrect Input")

    sleep(1)

    computer = randint(1, 3)
    if computer == 1:
        print("Computer has chosen Rock")
    elif computer == 2:
        print("Computer has chosen Paper")
    else:
        print("Computer has chosen Scissors")

    if player == computer:
        print("It's a draw!")
        data["draws"] += 1
    elif player == 1 and computer == 2:
        print("Computer has won!")
        data["loses"] += 1
    elif player == 1 and computer == 3:
        print("You have won!")
        data["wins"] += 1
    elif player == 2 and computer == 1:
        print("You have won!")
        data["wins"] += 1
    elif player == 2 and computer == 3:
        print("Computer has won!")
        data["loses"] += 1
    elif player == 3 and computer == 1:
        print("Computer has won!")
        data["loses"] += 1
    elif player == 3 and computer == 2:
        print("You have won!")
        data["wins"] += 1
    with open("data", "w+") as f:
        f.write(str(data))

    print('''
=========================
You have %d total wins
You have %d total loses
You have %d total draws

You have played %d times
=========================
''' % (data["wins"], data["loses"], data["draws"],
       data["wins"] + data["loses"] + data["draws"]))


def plagain():
    while True:
        again = input('''
"Type 'Yes' or 'No' if you either want to play again or close the program or
'Reset' to reset your score and close the program:''').lower()
        if again == "yes" or again == "y":
            main()
        elif again == "no" or again == "n":
            break
        elif again == "reset" or again == "r":
            with open("data", "w+") as f:
                f.write("{'wins': 0, 'loses': 0, 'draws': 0}")
            print("Score Reseted Successfully!")
            sleep(1)
            break
        else:
            print("Error:Incorrect Input")


if __name__ == "__main__":
    print("'Rock, Paper, Scissors' game by BouncyMaster")
    main()
    plagain()
