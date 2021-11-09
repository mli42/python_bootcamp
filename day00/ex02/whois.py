# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 15:29:38 by mli               #+#    #+#              #
#    Updated: 2021/11/06 16:13:56 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def quit(verbose: bool = True) -> None:
    if (verbose):
        print("ERROR")
    exit(1)


sys.argv.pop(0)
if (len(sys.argv) < 1):
    quit(False)
elif (len(sys.argv) > 1):
    quit()

try:
    nb = int(sys.argv[-1])
except ValueError:
    quit()

if (nb == 0):
    print("I'm Zero.")
elif (nb % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
