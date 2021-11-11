# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 16:26:01 by mli               #+#    #+#              #
#    Updated: 2021/11/11 11:44:54 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint as rand

NB_MIN = 1
NB_MAX = 99
isnum = True
count = 1
mys = rand(NB_MIN, NB_MAX)
guess = ""

def handleValueError() -> None:
    global isnum

    if (guess == 'exit'):
        exit("\tYou ran away.")
    print("That's not a number")
    isnum = False

"""
Ask the next guess from the player
"""
def askGuess(firstTime: bool = False) -> None:
    global guess
    global isnum

    askString = "Try again !\n>> "
    if (firstTime is True):
        askString = f"Try to guess an number between {NB_MIN} and {NB_MAX} ! Or 'exit'...\n>> "
    try:
        guess = input(askString)
        guess = int(guess)
        isnum = True
    except ValueError:
        handleValueError()

askGuess(firstTime = True)
while (guess != mys):
    if (isnum == False):
        pass
    elif (guess < mys):
        print("It's too low!")
    elif (guess > mys):
        print("It's too high!")

    askGuess()
    count += 1

if (mys == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if (count > 1):
    print("Nice, indeed it was %d and you won in %d attempts" %(mys, count))
else:
    print("Wow, first try ! Congrats")
