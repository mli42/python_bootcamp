# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 23:44:36 by mli               #+#    #+#              #
#    Updated: 2020/01/20 00:19:35 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image

class ScrapBooker:

    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        img = Image.fromarray(array)
        if (img.size[0] >= dimensions[0] + position[0] and img.size[1] >= dimensions[1] + position[1]):
            cropped = img.crop((position[1], position[0], dimensions[1], dimensions[0]))
            return (np.asarray(cropped))
        return (array)


'''
#Load Image
test_nparray = np.asarray(Image.open("../42AI.png"))
#img = Image.fromarray(test_nparray)
#img.show()

scrap = ScrapBooker()
# Crop Test
Image.fromarray(scrap.crop(test_nparray, (30, 100))).show()
#
'''
