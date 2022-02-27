# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 22:42:30 by mli               #+#    #+#              #
#    Updated: 2022/02/27 16:35:00 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from copy import deepcopy
from ImageProcessor import ImageProcessor

class ColorFilter:

    def __guard_ndarray(funct):
        def inner(*args, **kwargs):
            array = args[0]
            if not (isinstance(array, np.ndarray) and
            ('float' in str(array.dtype) or 'int' in str(array.dtype))):
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
        res = 1 - array
        res[..., 3:] = array[..., 3:]
        return res

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
        only_blue_green = ColorFilter.to_blue(array) + ColorFilter.to_green(array)

        res = array - only_blue_green
        res[..., 3:] = array[..., 3:]
        return res

    @staticmethod
    @__guard_ndarray
    def to_celluloid(array: np.ndarray) -> np.ndarray:
        bounds = np.linspace(array.min(), array.max(), 5)
        res = array.copy()

        lower_bound = bounds[0]
        for upper_bound in bounds[1:]:
            mask = (res[..., :3] > lower_bound) & (res[..., :3] < upper_bound)
            res[..., :3][mask] = lower_bound
            lower_bound = upper_bound
        return res

    @staticmethod
    def __guard_grayscale(filter: str, **kwargs) -> bool:
        weights = kwargs.get('weights')
        hasWeights = weights is not None

        if (
            (filter not in ['m', 'mean', 'w', 'weight']) or
            (filter in ['m', 'mean'] and hasWeights) or
            (not isinstance(weights, list)) or
            (len(weights) != 3) or
            (all([isinstance(obj, float) for obj in weights]))
          ):
            return False
        return True

    @staticmethod
    @__guard_ndarray
    def to_grayscale(array: np.ndarray, filter: str, **kwargs) -> np.ndarray:
        if ColorFilter.__guard_grayscale(filter, **kwargs) is False:
            return None
        return array


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
        base_ope = ('Base img', lambda x: x, [], {})
        arr = [
            base_ope,
            ('Inverted', cfilter.invert, [], {}),
            ('To blue', cfilter.to_blue, [], {}),
            ('To green', cfilter.to_green, [], {}),
            ('To red', cfilter.to_red, [], {}),
            ('To celluloid', cfilter.to_celluloid, [], {}),
            ('To grayscale m', cfilter.to_grayscale, ['m'], {}),
            ('To grayscale mean', cfilter.to_grayscale, ['mean'], {}),
            ('To grayscale w', cfilter.to_grayscale, ['w'], {'weights': [1., 2., 3.]}),
            ('To grayscale weight', cfilter.to_grayscale, ['weight'], {'weights': [1., 2., 3.]}),
            base_ope
        ]

        for label, fct, args, kwargs in arr:
            print(label)
            display_img(fct(img, *args, **kwargs))

    def grayscale_err(img):
        arr = [
            ('Args err', ['hey'], {'weights': [1., 2., 3.]}),
            ('Kwargs err', ['m'], {'hey': 123}),
            ('Weight value', ['m'], {'weights': 123}),
            ('Mean with weight', ['m'], {'weights': [1., 2., 3.]}),
        ]
        for label, args, kwargs in arr:
            print(label)
            display_img(cfilter.to_grayscale(img, *args, **kwargs))

    print('Trying with Elon')
    launch_filters(elon)
    print('Trying with inverted Elon')
    launch_filters(cfilter.invert(elon))
    print('Check grayscale guardian')
    grayscale_err(elon)

if __name__ == "__main__":
    main()
