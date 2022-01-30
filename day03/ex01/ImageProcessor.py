# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 21:40:16 by mli               #+#    #+#              #
#    Updated: 2022/01/30 17:21:55 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpltimg
from sys import stderr

class ImageProcessor:

    def __init__(self):
        pass

    @staticmethod
    def load(path: str) -> np.ndarray or None:
        img = None
        try:
            img = mpltimg.imread(path)
            print("The dimensions of the image are %d x %d." %(img.shape[0], img.shape[1]))
        except Exception as e:
            print(f"Exception: {e.__class__.__name__}: {e.strerror if hasattr(e, 'strerror') else e}", file=stderr)
        return (img)

    @staticmethod
    def display(array: np.ndarray):
        if not isinstance(array, np.ndarray):
            print("ImgProcessor.display: Parameter is not a numpy array", file=stderr)
            return
        plt.axis("off")
        plt.imshow(array)
        plt.show()

def main():
    imgProcessor = ImageProcessor()
    def test_img(path: str):
        print(f"Loading path: {path}")
        img_array = imgProcessor.load(path)
        print("Loading returned:", img_array)
        if (img_array is not None):
            imgProcessor.display(img_array)

    test_img("../resources/42AI.png")
    test_img("../resources/coucou.png")
    test_img("../resources/couco.png")

if __name__ == "__main__":
    main()
