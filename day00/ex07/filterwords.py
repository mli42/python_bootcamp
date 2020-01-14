# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 14:51:41 by mli               #+#    #+#              #
#    Updated: 2020/01/14 15:04:16 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.argv.pop(0)
if (len(sys.argv) != 2):
    exit(print("Wrong number of args \!"))

try:
    string = str(sys.argv[0])
    max_len = int(sys.argv[1])
except ValueError:
    exit(print("Wrong types of arguments"))

splited = string.split()

for tmp in splited:
    for words in splited:
        if (len(words) <= max_len):
            splited.remove(words)
print(splited)
