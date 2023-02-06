
# Sayı Tahmin Oyunu
import random
import time


def Game():
    
    number = random.randint(0, 20)
    count = 0
    user = 0
    
    print("----\  Welcome to Number Guessing Game  /----\n")
    print("Steven: Heyy! Welcome!\n Steven: I'm Steven. \n Steven: I will give you brief information while playing the game\n")

    while (True):
        user = input("Enter Your Guess: ")
        count = count + 1
        user = int(user)

        if (user > number):
            print("Steven:UHHH!\nSteven: it's hot around here try a smaller number please!")

        elif (user < number):
            print("Steven: UHHH!\nSteven: it's cold around here try a bigger number please")

        elif (user == "E"):
            print("Exited To Game...")
            time.sleep(3)
            print("Good Bye...")
            break

        else:
            print("Steven: Congratulations! \nSteven: You Guessed the Number Correctly!")
            print("Steven: Number of Guesses = ", str(count))
            print("Steven: It was so nice to play with you.!.\nSteven: Hope to see you in the new game. See you...")
            time.sleep(3)
            break

Game()
