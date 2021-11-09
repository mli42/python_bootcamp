# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 16:15:10 by mli               #+#    #+#              #
#    Updated: 2021/11/09 18:01:58 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

class charType():
    UPPER = 0
    LOWER = 1
    PUNC = 2
    SPACE = 3
    LEN = 4


def text_analyzer(entry: str = None) -> None:
    '''
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    '''

    ulps = [0] * charType.LEN
    if entry is None:
        entry = ""
        for line in sys.stdin:
            entry += line.rstrip('\n')
    for char in entry:
        if char.isupper():
            ulps[charType.UPPER] += 1
        elif char.islower():
            ulps[charType.LOWER] += 1
        elif char in string.punctuation:
            ulps[charType.PUNC] += 1
        elif char.isspace():
            ulps[charType.SPACE] += 1
    print("The text contains %d characters:" % len(entry))
    print("- %d upper letters" % ulps[charType.UPPER])
    print("- %d lower letters" % ulps[charType.LOWER])
    print("- %d punctuation marks" % ulps[charType.PUNC])
    print("- %d spaces" % ulps[charType.SPACE])


"""
text_analyzer("Python 2.0, released 2000, introduced features \
like List comprehensions and a garbage collection system capable of \
collecting reference cycles.")
"""
