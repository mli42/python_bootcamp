# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 00:37:29 by mli               #+#    #+#              #
#    Updated: 2020/01/14 00:41:56 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

date = (3, 30, 2019, 9, 25)


print("%02d/%02d/%04d %02d:%02d" %(date[-2], date[-1], date[-3], date[0], date[1]))
