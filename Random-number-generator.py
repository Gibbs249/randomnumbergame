# Hello, my name is Gibbs!
# Welcome to my random number game. Try your best to guess the generated number!

# Establish imports
import random


# Set up algorithm for main game
def game():
    print('This time I will give you... ' + str(tries) + ' tries.')
    print('Type a number and hit Enter to guess!')
    rando = random.randint(1, 20)
    playernum = 21000
    while rando != playernum:
        i = 0
        while i != tries:
            try:
                playernum = int(input())
            except ValueError:
                print('You cannot trick me. Please enter a number.')
                continue
            i += 1
            if playernum > rando:
                print('It looks like ' + str(playernum) + ' is too high')
            elif playernum < rando:
                print('It looks like ' + str(playernum) + ' is too low.')
            else:
                print('Congratulations! After ' + str(i) + ' tries, ' + str(
                    rando) + ' is the correct guess!')
                print('How about another game ' + name + '?')
                break
        else:
            print('It looks like you have run out of tries.')
            print(str(rando) + ' is the correct answer! Better luck next time!')
            print('How about another game ' + name + '?')
            break


# Setup. Runs once to establish name and start first round.
tries = random.randint(3, 7)
print('Hello, what is your name?')
name = input()
print('Nice to meet you ' + name + '!')
print('I am thinking of a number between 1 and 20.')
print('Try to guess what number it is!')
game()

# While loop to input another round or end the program.
while tries != 0:
    print('Type Y for yes and N for no. Then hit Enter.')
    again = input();
    if again.upper() == 'Y':
        game()
    elif again.upper() == 'N':
        print('You are free to exit the game, thank you for playing!')
        break
    else:
        print('That is not a valid input.')
        continue
