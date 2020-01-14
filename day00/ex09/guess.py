# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 16:26:01 by mli               #+#    #+#              #
#    Updated: 2020/01/14 17:18:38 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint as rand

isnum = 1
count = 1
mys = rand(0, 99)

try:
    nb = input("Try to guess an number between 0 and 99 ! Or 'exit'...\n>> ")
    nb = int(nb)
except ValueError:
    exit("\tYou ran away.") if (nb == 'exit') else print("That's not a number")
    isnum = 0

while (nb != mys):
    if (nb < mys and isnum == 1):
        print("It's too low!")
    elif (nb > mys and isnum == 1):
        print("It's too high!")
    try:
        if (count % 3 == 0):
            print("You can write 'exit' in order to giveup...")
        nb = input("Try again !\n>> ")
        nb = int(nb)
    except ValueError:
        exit("\tYou ran away.") if (nb == 'exit') else print("That's not a number")
        isnum = 0
    count += 1

if (mys == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")
if (count > 1):
    print("Nice, indeed it was %d and you did it with %d attempts" %(mys, count))
else:
    print("Wow, first try ! Congrats")
