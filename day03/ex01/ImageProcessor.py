# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 21:40:16 by mli               #+#    #+#              #
#    Updated: 2020/01/19 23:35:39 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image

class ImageProcessor:

    @staticmethod
    def load(path):
        img = Image.open(path)
        print("The dimensions of the image are %d x %d." %(img.size[0], img.size[1]))
        return (np.asarray(img))

    @staticmethod
    def display(array):
        img = Image.fromarray(array)
        img.show()

'''
test = ImageProcessor()
img_array = test.load("../42AI.png")
test.display(img_array)
'''
