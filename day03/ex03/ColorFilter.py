# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 22:42:30 by mli               #+#    #+#              #
#    Updated: 2022/02/06 00:56:15 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from copy import deepcopy
from ImageProcessor import ImageProcessor

class ColorFilter:

    def __guard_ndarray(funct):
        def inner(*args, **kwargs):
            array = args[0]
            if not (isinstance(array, np.ndarray) and array.dtype == 'float32'):
                return None
            try:
                return_value = funct(*args, **kwargs)
            except:
                return None
            return return_value
        return (inner)

    @staticmethod
    @__guard_ndarray
    def invert(array: np.ndarray) -> np.ndarray:
        return 1 - array[..., :3]

    @staticmethod
    @__guard_ndarray
    def to_blue(array: np.ndarray) -> np.ndarray:
        res = np.zeros(array.shape)
        res[..., 2:] = array[..., 2:]
        return res

    @staticmethod
    @__guard_ndarray
    def to_green(array: np.ndarray) -> np.ndarray:
        res = deepcopy(array)
        res[..., :3:2] = res[..., :3:2] * 0
        return res

    @staticmethod
    @__guard_ndarray
    def to_red(array: np.ndarray) -> np.ndarray:
        self = ColorFilter()
        res = array[..., :3] - (self.to_blue(array) + self.to_green(array))[..., :3]
        return res

def main():
    imgProc = ImageProcessor()
    cfilter = ColorFilter()
    elon = imgProc.load("../resources/elon.png")

    def display_img(array):
        if array is None:
            print('Array is None')
            return
        imgProc.display(array)

    def launch_filters(img):
        if img is None:
            print('Img is None')
            return
        print('Base img')
        display_img(img)
        print('Inverted')
        display_img(cfilter.invert(img))
        print('To blue')
        display_img(cfilter.to_blue(img))
        print('To green')
        display_img(cfilter.to_green(img))
        print('To red')
        display_img(cfilter.to_red(img))
        print('Base img')
        display_img(img)

    print('Trying with Elon')
    launch_filters(elon)
    print('Trying with inverted Elon')
    launch_filters(cfilter.invert(elon))

if __name__ == "__main__":
    main()
