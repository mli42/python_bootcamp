# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/16 23:13:39 by mli               #+#    #+#              #
#    Updated: 2020/01/17 00:30:11 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def my_randfct(words):
    width = len(words)
    my_rand = int(width / 1.3)
    my_rand = (width - my_rand if (width - my_rand > 0 and width - my_rand < width) else -1)
    if (width == 0):
        return ('w')
    if (width % 3 == 0):
        return (words[-my_rand - int(my_rand / 1.3)])
    if (width % 2 == 0):
        return (words[-int(my_rand / 1.6)])
    return (words[my_rand])

def generator(text, sep=" ", option=None):
    try:
        test = 'text'
        text = str(text)
        test = 'separator'
        sep = str(sep)
        test = 'option'
        if (option != 'shuffle' and option != 'unique' and option != 'ordered' and option != None):
            int("Not work")
    except ValueError:
        return("ERROR")

    lst = text.split(sep)

    if (option == 'shuffle'):
        lst.sort(key=my_randfct)
    elif (option == 'unique'):
        lst.reverse()
        for words in lst:
            if (lst.count(words) > 1):
                lst.remove(words)
        lst.reverse()
    elif (option == 'ordered'):
        lst.sort()

    for words in lst:
        yield (words)


#for words in generator("Helloooo how are you ? Im lokking  if it ! works well or not", option='shuffle'):
#    print("- '%s'" %words)

#for words in generator("Helloooo how are you ?  a if it ! works well or not or a if", option='unique'):
#    print("- '%s'" %words)

#for words in generator("Helloooo how are you ?  a if it ! works well or not or a if", option='ordered'):
#    print("- '%s'" %words)
