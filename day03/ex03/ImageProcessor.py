# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 21:40:16 by mli               #+#    #+#              #
#    Updated: 2020/11/24 22:41:40 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpltimg

class ImageProcessor:

    @staticmethod
    def load(path):
        img = mpltimg.imread(path)
        print("The dimensions of the image are %d x %d." %(img.shape[0], img.shape[1]))
        return (img)

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()

if __name__ == "__main__":
    test = ImageProcessor()
    img_array = test.load("../resources/42AI.png")
    test.display(img_array)
