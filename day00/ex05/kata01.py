# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 00:24:46 by mli               #+#    #+#              #
#    Updated: 2020/01/14 00:34:12 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
        "Python": "Guido van Rossum",
        "Ruby": "Yukihiro Matsumoto",
        "PHP": "Rasmus Lerdorf",
        }

for x in languages:
    print(x + " was created by " + languages[x])
