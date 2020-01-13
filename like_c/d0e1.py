# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 14:04:18 by mli               #+#    #+#              #
#    Updated: 2020/01/13 15:09:49 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

reversed_str = []
argc = len(sys.argv)

for i in range(1, argc):
    arg = sys.argv[argc - i]
    index = len(arg)
    while (index > 0):
        reversed_str += arg[index - 1]
        index -= 1
print (str(reversed_str).swapcase())
