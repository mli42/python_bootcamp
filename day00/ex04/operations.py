# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 23:28:45 by mli               #+#    #+#              #
#    Updated: 2020/01/14 00:04:07 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def UseError(str=None):
    if (str != None):
        print("InputError: " + str + "\n")
    print("Usage: python operations.py")
    print("Example:\n\tpython operations.py 10 3")
    exit()

sys.argv.pop(0)
if (len(sys.argv) != 2):
    UseError("Wrong number of arguments")

try:
    a = int(sys.argv[0])
    b = int(sys.argv[1])
except ValueError:
    UseError("Only numbers in input")

print("Sum:\t\t%d" %(a + b))
print("Difference:\t%d" %(a - b))
print("Product:\t%d" %(a * b))
print("Quotient:\t", end="")
print("%f" %(a / b)) if (b != 0) else print("ERROR (div by zero)")
print("Remainder:\t", end="")
print("%d" %(a % b)) if (b != 0) else print("ERROR (mod by zero)")
