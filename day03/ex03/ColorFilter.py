# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/24 22:42:30 by mli               #+#    #+#              #
#    Updated: 2020/11/24 23:34:25 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpltim
from ImageProcessor import ImageProcessor

class ColorFilter:

	@staticmethod
	def invert(array: np.ndarray) -> np.ndarray:
		return array

if __name__ == "__main__":
	imgProc = ImageProcessor()
	cfilter = ColorFilter()
	elon = imgProc.load("../resources/elon.png")
	#imgProc.display(elon)

	imgProc.display(cfilter.invert(elon))
