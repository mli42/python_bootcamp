# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 00:44:47 by mli               #+#    #+#              #
#    Updated: 2020/11/11 21:48:57 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

phrase = "The right format"

dashs = 42 - len(phrase)
print(("-" * dashs) + phrase, end="")
