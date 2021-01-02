# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 16:58:07 by mli               #+#    #+#              #
#    Updated: 2021/01/02 18:41:05 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from mylinearregression import MyLinearRegression as MyLR
from ridge import MyRidge as MyLRR

if __name__ == "__main__":
    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
    Y = np.array([[23.], [48.], [218.]])
    mylr = MyLRR([[1.], [1.], [1.], [1.], [1]], 5e-5, int(3e+5))


    # Example 0:
    Y_hat = mylr.predict_(X)
    print(Y_hat)
    # Output: array([[8.], [48.], [323.]])

    # Example 1:
    print(mylr.cost_(Y_hat, Y))
    # Output: 1875.0

    mylr.fit_(X, Y)
    print(mylr.thetas)

    Y_hat = mylr.predict_(X)
    print(Y_hat)

    print(mylr.cost_(Y_hat, Y))
