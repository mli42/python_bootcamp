# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:07:11 by mli               #+#    #+#              #
#    Updated: 2021/11/28 00:04:13 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    """Class representing a GoT Character

    Args:
        first_name: string = None
        is_alive: bool = True
    """
    def __init__(self, first_name: str = None, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """Class representing a GoT Character from the Stark family

    Args:
        first_name: string = None
        is_alive: bool = True
    Attributes:
        family_name: string = "Stark"
        house_words: string = "Winter is Coming"
    """
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super(Stark, self).__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
    print(arya.__doc__)
    print(GotCharacter.__doc__)
