# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 15:22:51 by mli               #+#    #+#              #
#    Updated: 2020/01/17 17:18:26 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import inspect
import time
from random import randint

fcts = ["start_machine", "boil_water", "make_coffee", "add_watter"]

def log(*fct):

    def inner(*args, **kwargs):
        f = open("machine.log", 'w')
        if (inspect.stack()[1].function == 'make_coffee'):
            f.write(inspect.stack()[1].function)
        f.close()
        return (fct[0](*args, **kwargs))
    
    return (inner)


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)


