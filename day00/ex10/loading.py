# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/20 22:12:23 by mli               #+#    #+#              #
#    Updated: 2020/11/20 23:27:05 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

def ft_progress(lst):
    BARLEN = 23
    LSTLEN = len(lst)
    STARTTIME = time.time()
    eta = 3.4
    for i, elem in enumerate(lst, 1):
        ratio = i / LSTLEN
        percentage = ratio * 100
        bar = ("=" * int(ratio * (BARLEN - 1))) + ">"
        current_time = time.time()
        elapsed = current_time - STARTTIME
        print("\rETA: %.2fs [%3d%%][%-*s] %d/%d | elapsed time %.2fs"
              %(eta, percentage, BARLEN, bar, i, LSTLEN, elapsed), end="")
        yield (elem)

if __name__ == "__main__":

    ret = 0
    if False:
        listy = range(1000)
        for elem in ft_progress(listy):
            ret += (elem + 3) % 5
            time.sleep(0.01)
    else:
        listy = range(3333)
        for elem in ft_progress(listy):
            ret += elem
            time.sleep(0.005)
    print()
    print(ret)
