# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 14:51:41 by mli               #+#    #+#              #
#    Updated: 2021/11/11 17:03:55 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

PUNCT = string.punctuation

if (len(sys.argv) != 3):
    exit("Wrong number of args!")

try:
    txt = str(sys.argv[1])
    max_len = int(sys.argv[2])
except ValueError:
    exit("Wrong types of arguments")

# Replace every punctuation by a space
txt = txt.translate(str.maketrans(PUNCT, ' ' * len(PUNCT)))
splited = txt.split()
res = [word for word in splited if len(word) > max_len]

print(res)
