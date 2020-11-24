# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 23:44:36 by mli               #+#    #+#              #
#    Updated: 2020/11/24 12:07:23 by mli              ###   ########.fr        #
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
        axis=int(not axis)
        index_to_delete = list(range(n - 1, array.shape[axis], n))
        made_thinner = np.delete(array, index_to_delete, axis=axis)
        return made_thinner

    @staticmethod
    def juxtapose(array, n, axis):
        res = np.copy(array)
        for i in range(n):
            res = np.concatenate((res, array), axis=axis)
        return res

    def mosaic(self, array, dimensions):
        res = self.juxtapose(array, dimensions[0] - 1, 0)
        res = self.juxtapose(res, dimensions[1] - 1, 1)
        return res

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
    showimg(scrap.mosaic(img42ai, (2, 3)))
