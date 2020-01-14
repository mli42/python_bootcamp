# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 00:48:37 by mli               #+#    #+#              #
#    Updated: 2020/01/14 01:21:52 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#t = (0, 4, 132.42222, 10000, 12345.67)
t = (0, 4, 132.42222, 0.000123, -12345.67)

def sci_writting(nb=None):
    power = 0
    sign = (1 if (nb >= 0) else -1)
    nb *= (1 if (nb >= 0) else -1)
    great = (1 if (nb >= 1) else 0)
    while (nb > 9 or nb < 1):
        nb = ((nb / 10) if (great == 1) else (nb * 10))
        power += 1
    if (sign == -1):
        print("-", end='')
    print("%.2fe" %nb, end="")
    print("+", end="") if (great == 1) else print("-", end='')
    print("%02d" %power, end="")

print("day_%02d, ex_%02d : %.2f, " %(t[0], t[1], t[2]), end="")
sci_writting(t[3])
print(", ", end="")
sci_writting(t[4])
print("")
