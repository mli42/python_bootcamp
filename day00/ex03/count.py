# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 16:15:10 by mli               #+#    #+#              #
#    Updated: 2020/01/13 19:08:48 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(text=None):
    if (text == None):
        exit(text_analyzer(input("No text given. What's the text to analyse?\n\
You can write '__DOC__' in order to read the doc : ")))
    if (text == "__DOC__"):
        exit(print("\n\tThis function counts the number of upper characters, \
lower characters, punctuation and spaces in a given text."))
    text = str(text)
    if (text.isprintable() == False):
        exit(print("Not printable text"))
    up_chars = 0
    low_chars = 0
    punct_chars = 0
    sp_chars = 0
    for chars in text:
        if (chars.islower()):
            low_chars += 1
        elif (chars.isupper()):
            up_chars += 1
        elif (chars.isspace()):
            sp_chars += 1
        elif (chars.find("!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~") and
                chars.isdigit() == False):
            punct_chars += 1
    print("The text contains %d characters:" %(len(text)))
    print("- %d upper letters" %up_chars)
    print("- %d lower letters" %low_chars)
    print("- %d punctuation marks" %punct_chars)
    print("- %d spaces" %sp_chars)
