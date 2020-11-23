# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 23:44:36 by mli               #+#    #+#              #
#    Updated: 2020/11/23 23:02:38 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpltimg

class ScrapBooker:

    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        img = array
        border_max = (position[0] + dimensions[0], position[1] + dimensions[1])
        if (img.shape[0] >= border_max[0] and img.shape[1] >= border_max[1]):
            cropped = img[position[0]:border_max[0], position[1]:border_max[1]]
            return (cropped)
        # If out of bounds, returns original img?
        return (array)

    @staticmethod
    def thin(array, n, axis):
        axis=not axis # Because np and asked axis are inversed
        index_to_delete = list(range(n - 1, array.shape[axis], n))
        made_thinner = np.delete(array, index_to_delete, axis=axis)
        return made_thinner

def showimg(array):
    plt.imshow(array)
    plt.show()

if __name__ == "__main__":
    scrap = ScrapBooker()
    path = "../resources/42AI.png"
    img42ai = mpltimg.imread(path)
    #showimg(img42ai)

    # Crop Test
    showimg(scrap.crop(img42ai, (30, 200), (140, 0)))
