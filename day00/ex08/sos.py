# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 15:12:28 by mli               #+#    #+#              #
#    Updated: 2020/01/14 16:20:28 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.argv.pop(0)

try:
    args = list(sys.argv)
except ValueError:
    exit(print("ERROR"))

morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
            'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
            'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
            'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--','X':'-..-',
            'Y':'-.--', 'Z':'--..', ' ' : '/',
            '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
            '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

for words in args:
    if (words in morse_dict.keys() == False):
        exit(print("ERROR"))

i = 0
size = len(args)

for words in args:
    words = words.upper()
    j = 0
    lenght = len(words)
    for chars in words:
        print(morse_dict[chars], end="")
        if (j != lenght - 1):
            print(" ", end='')
        j += 1
    if (i != size - 1):
        print(" / ", end='')
    i += 1
print("")
