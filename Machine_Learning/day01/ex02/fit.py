# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 23:34:26 by mli               #+#    #+#              #
#    Updated: 2020/01/21 23:49:19 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def fit_(theta, X, Y, alpha, n_cycle):
    pass

"""Description:
        Performs a fit of Y(output) with respect to X.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
        Y: has to be a numpy.ndarray, a vector of dimension (number of training examples, 1).
        alpha : un float positif
        n_cycle : un integer positif
    Returns:
        new_theta: numpy.ndarray, a vector of dimension (number of the features +1,1).
        None if there is a matching dimension problem.


        Les delta arrondis signifie que l’on prend la dérivée partielle
        le terme signifie que tu multiplies -alpha par la dérivée partielle suivant theta_j de la fonction J
"""
