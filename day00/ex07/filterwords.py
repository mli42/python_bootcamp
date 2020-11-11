# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 14:51:41 by mli               #+#    #+#              #
#    Updated: 2020/11/11 22:22:20 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 3):
    exit(print("Wrong number of args \!"))

try:
    string = str(sys.argv[1])
    max_len = int(sys.argv[2])
except ValueError:
    exit(print("Wrong types of arguments"))

splited = [word.strip("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~") for word in string.split()]
res = [word for word in splited if len(word) > max_len]

print(res)
