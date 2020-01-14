# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 00:10:32 by mli               #+#    #+#              #
#    Updated: 2020/01/14 00:23:56 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = tuple((19, 42, 21))

size = len(t)
if (size == 0):
    exit(print("No number in entry"))

print("The %d numbers are: " %size, end="") if (size > 0) else print("The number is: ", end="")
for i in range(0, size):
    print(t[i], end="")
    if (i != size - 1):
        print(", ", end="")
print("")
