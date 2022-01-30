# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 23:44:36 by mli               #+#    #+#              #
#    Updated: 2022/01/30 18:09:06 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from ImageProcessor import ImageProcessor

class ScrapBooker:

    def __init__(self):
        pass

    @staticmethod
    def __guard_array(array: np.ndarray) -> bool:
        if not (isinstance(array, np.ndarray)):
            return False
        return True

    @staticmethod
    def __guard_shape(shape: tuple) -> bool:
        if not (isinstance(shape, tuple) and len(shape) == 2
        and all([(isinstance(obj, int) and obj >= 0) for obj in shape])):
            return False
        return True

    def crop(self, array: np.ndarray, dim: tuple, position: tuple = (0, 0)) -> np.ndarray or None:
        if not (self.__guard_array(array) and
        self.__guard_shape(dim) and
        self.__guard_shape(position)):
            return None

        border_max = (position[0] + dim[0], position[1] + dim[1])
        if not (array.shape[0] >= border_max[0] and array.shape[1] >= border_max[1]):
            return None
        cropped = array[position[0]:border_max[0], position[1]:border_max[1]]
        return cropped

    def thin(self, array: np.ndarray, n: int, axis: int) -> np.ndarray or None:
        if not (self.__guard_array(array) and
        isinstance(n, int) and n > 0 and
        isinstance(axis, int) and (axis == 0 or axis == 1)):
            return None

        axis=int(not axis)
        index_to_delete = list(range(n - 1, array.shape[axis], n))
        made_thinner = np.delete(array, index_to_delete, axis=axis)
        return made_thinner

    def juxtapose(self, array: np.ndarray, n: int, axis: int) -> np.ndarray or None:
        if not (self.__guard_array(array) and
        isinstance(n, int) and n > 0 and
        isinstance(axis, int) and (axis == 0 or axis == 1)):
            return None

        res = np.copy(array)
        for i in range(n - 1):
            res = np.concatenate((res, array), axis=axis)
        return res

    def mosaic(self, array: np.ndarray, dim: tuple) -> np.ndarray or None:
        if not (self.__guard_array(array) and self.__guard_shape(dim)):
            return None

        res = self.juxtapose(array, dim[0], 0)
        res = self.juxtapose(res, dim[1], 1)
        return res

def main():
    scrap = ScrapBooker()
    img_processor = ImageProcessor()
    img42ai = img_processor.load("../resources/42AI.png")
    def display_img(array):
        if (array is None):
            print("Array is None")
        else:
            img_processor.display(array)

    arr1 = np.arange(0,25).reshape(5,5)
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
    arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

    display_img(img42ai)

    print("--- Crop")
    display_img(scrap.crop(img42ai, (30, 200), (140, 0)))
    print(scrap.crop(arr1, (3,1),(1,0)))

    print("--- Mosaic")
    display_img(scrap.mosaic(img42ai, (2, 3)))
    display_img(scrap.mosaic(img42ai, (3, 2)))

    print("--- Thin")
    print(scrap.thin(arr2, 3, 0))
    print(scrap.thin(arr3, 3, 1))

    print("--- Juxtapose")
    print(scrap.juxtapose(arr4, 2, 0))
    print(scrap.juxtapose(arr4, 2, 1))

    print("--- Error Management")
    display_img(scrap.crop(img42ai, (30, 300), (140, 0)))
    display_img(scrap.crop(img42ai, (30, 200), [140, 0]))
    print(scrap.crop([[1, 2, 3],[4, 5, 6],[7, 8, 9]], (1,2)))
    print(scrap.juxtapose(arr4, -2, 0))
    print(scrap.mosaic(arr4, (1, 2, 3)))

if __name__ == "__main__":
    main()
