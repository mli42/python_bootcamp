# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 21:40:16 by mli               #+#    #+#              #
#    Updated: 2020/11/23 00:25:03 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image

# May need: pip install Pillow

class ImageProcessor:

    @staticmethod
    def load(path):
        with Image.open(path) as img:
            print("The dimensions of the image are %d x %d." %(img.size[0], img.size[1]))
            ret = np.asarray(img)
        return (ret)

    @staticmethod
    def display(array):
        img = Image.fromarray(array)
        img.show()

if __name__ == "__main__":
    test = ImageProcessor()
    img_array = test.load("../resources/42AI.png")
    test.display(img_array)
