# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 22:42:30 by mli               #+#    #+#              #
#    Updated: 2022/03/12 23:30:33 by mli              ###   ########.fr        #
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
        weights = kwargs.pop('weights', None)
        hasWeights = weights is not None

        if (
            (len(kwargs) != 0) or
            (filter not in ['m', 'mean', 'w', 'weight']) or
            (filter in ['m', 'mean'] and hasWeights) or
            (filter in ['w', 'weight'] and (
                not isinstance(weights, list) or
                len(weights) != 3 or
                not all([isinstance(obj, float) and obj >= 0 for obj in weights]) or
                np.sum(weights) != 1.
                ))
          ):
            return False
        return True

    @staticmethod
    @__guard_ndarray
    def to_grayscale(array: np.ndarray, filter: str, **kwargs) -> np.ndarray:
        if ColorFilter.__guard_grayscale(filter, **kwargs) is False:
            return None
        weights = kwargs.get('weights')
        res = array.copy()

        if (filter in ['m', 'mean']):
            mono = np.sum(res[..., :3], axis=2, keepdims=True) / 3
            res = np.dstack((np.tile(mono, 3), res[..., 3:]))
        elif (filter in ['w', 'weight']):
            res[..., 0] *= weights[0]
            res[..., 1] *= weights[1]
            res[..., 2] *= weights[2]
            mono = np.sum(res[..., :3], axis=2, keepdims=True)
            res = np.dstack((np.tile(mono, 3), res[..., 3:]))
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
            ('To grayscale w', cfilter.to_grayscale, ['w'], {'weights': [.2, .3, .5]}),
            ('To grayscale weight', cfilter.to_grayscale, ['weight'], {'weights': [.6, .2, .2]}),
            base_ope
        ]

        for label, fct, args, kwargs in arr:
            print(label)
            display_img(fct(img, *args, **kwargs))

    def grayscale_err(img):
        arr = [
            ('Args err', ['hey'], {'weights': [.8, .1, .1]}),
            ('Kwargs err', ['m'], {'hey': 123}),
            ('Weight value', ['m'], {'weights': 123}),
            ('Mean with weight', ['m'], {'weights': [.8, .1, .1]}),
            ('Weight tuple', ['w'], {'weights': (.8, .1, .1)}),
            ('Weight intruder', ['w'], {'weights': [1., 2., 'a']}),
            ('Too much float', ['w'], {'weights': [.8, .1, .1, .0]}),
            ('Too high float', ['w'], {'weights': [.8, .1, .2]}),
            ('Too much kwargs', ['w'], {'weights': [.8, .1, .1], 'hey': 'a'}),
            ('Negativ float', ['w'], {'weights': [.8, -.1, .3]}),
        ]
        for label, args, kwargs in arr:
            print(label, end=': ')
            display_img(cfilter.to_grayscale(img, *args, **kwargs))

    print('Trying with Elon')
    launch_filters(elon)
    print('Trying with inverted Elon')
    launch_filters(cfilter.invert(elon))
    print('Check grayscale guardian')
    grayscale_err(elon)

if __name__ == "__main__":
    main()
