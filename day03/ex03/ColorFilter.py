# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 22:42:30 by mli               #+#    #+#              #
#    Updated: 2020/11/25 22:57:33 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.image as mpltim
from ImageProcessor import ImageProcessor

class ColorFilter:

	@staticmethod
	def invert(array: np.ndarray) -> np.ndarray:
		return np.asarray([1., 1., 1.]) - array[..., :3]

	@staticmethod
	def to_blue(array: np.ndarray) -> np.ndarray:
		res = np.zeros(array.shape)
		res[..., 2] = array[..., 2]
		res[..., 3] = array[..., 3]
		return res

	@staticmethod
	def to_green(array: np.ndarray) -> np.ndarray:
		res = [0, 1, 0, 1] * array
		return res

	@staticmethod
	def to_red(array: np.ndarray) -> np.ndarray:
		self = ColorFilter()
		res = array[..., :3] - (self.to_blue(array) + self.to_green(array))[..., :3]
		return res

if __name__ == "__main__":
	imgProc = ImageProcessor()
	cfilter = ColorFilter()
	elon = imgProc.load("../resources/elon.png")
	#imgProc.display(elon)

	#imgProc.display(cfilter.invert(elon))
	#imgProc.display(cfilter.to_blue(elon))
	#imgProc.display(cfilter.to_green(elon))
	#imgProc.display(cfilter.to_red(elon))
	#imgProc.display(elon)
