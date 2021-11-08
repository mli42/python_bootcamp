# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 23:28:45 by mli               #+#    #+#              #
#    Updated: 2021/11/08 22:53:54 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

argc = len(sys.argv)

def UseError(string: str = None) -> None:
    if (string != None):
        print(f"InputError: {string}\n")
    print(f"Usage: python {sys.argv[0]} <number1> <number2>")
    print(f"Example:\n\tpython {sys.argv[0]} 10 3")
    exit(1)

if (argc < 3):
    UseError()
elif (argc > 3):
    UseError("too many arguments")

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    UseError("only numbers")

print("Sum:\t\t%d" %(a + b))
print("Difference:\t%d" %(a - b))
print("Product:\t%d" %(a * b))
print("Quotient:\t", end="")
print(f"{a / b}" if (b != 0) else "ERROR (div by zero)")
print("Remainder:\t", end="")
print(f"{a % b}" if (b != 0) else "ERROR (mod by zero)")
