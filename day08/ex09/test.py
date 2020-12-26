# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/26 18:14:12 by mli               #+#    #+#              #
#    Updated: 2020/12/26 18:49:06 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from my_logistic_regression import MyLogisticRegression as MyLR

if __name__ == "__main__":
    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
    Y = np.array([[1], [0], [1]])
    mylr = MyLR([2, 0.5, 7.1, -4.3, 2.09], max_iter=int(2e4))

    # Example 0:
    Y_HAT = mylr.predict_(X)
    print(Y_HAT)
    # Output:
    """
    array([[0.99930437],
           [1.        ],
           [1.        ]])
    """

    # Example 1:
    print(mylr.cost_(Y, Y_HAT))
    # Output:
    """
    11.513157421577004
    """

    # Example 2:
    mylr.fit_(X, Y)
    print(mylr.theta)
    # Output:
    """
    [[ 4.81201635]
     [-1.32965333]
     [ 4.4887675 ]
     [-3.34153966]
     [ 0.43722784]]
    """

    # Example 3:
    Y_HAT = mylr.predict_(X)
    print(Y_HAT)
    # Output:
    """
    [[0.9308445 ]
     [0.45404475]
     [0.33497398]]
    """

    # Example 4:
    print(mylr.cost_(Y, Y_HAT))
    # Output:
    """
    0.590194577934653
    """
