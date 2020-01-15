# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:07:11 by mli               #+#    #+#              #
#    Updated: 2020/01/15 17:36:47 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        if (first_name == None):
            exit(print("Error, no name given"))
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super(Stark, self).__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
