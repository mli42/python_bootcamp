# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 15:29:38 by mli               #+#    #+#              #
#    Updated: 2020/01/13 16:54:58 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.argv.pop(0)
if (len(sys.argv) != 1):
    exit(print("ERROR"))

try:
    nb = int(sys.argv[-1])
except ValueError:
    exit(print("Error, not an integer"))

if (nb == 0):
    print("I'm Zero.")
elif (nb % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
