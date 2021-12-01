# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/16 23:13:39 by mli               #+#    #+#              #
#    Updated: 2021/12/01 22:33:55 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import random

def generator(text, sep=" ", option=None):
    if not isinstance(text, str) or not isinstance(sep, str) \
        or option not in [None, "shuffle", "unique", "ordered"]:
        yield ("ERROR")
        return

    lst = text.split(sep)

    if (option == 'shuffle'):
        lst.sort(key=lambda x: random())
    elif (option == 'unique'):
        lst = [word for i,word in enumerate(lst) if lst[:i].count(word) == 0]
    elif (option == 'ordered'):
        lst.sort()

    for words in lst:
        yield (words)

if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    for words in generator(text):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
    for words in generator(text, option='shuffle'):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
    for words in generator(text, option='ordered'):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
    for words in generator("3 lorem 3.4 lorem 4 ipsum 4.5 ipsum 5", option='unique'):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
    for words in generator(3.4, option='ordered'):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
    for words in generator("Lorem ipsum", sep=3.4, option='ordered'):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
    for words in generator("Lorem ipsum", option='Lorem ipsum too'):
        print("- '%s'" %words)
    print("---------------------------------------------------------------")
