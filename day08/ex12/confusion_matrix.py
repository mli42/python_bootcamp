# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    confusion_matrix.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/29 18:17:16 by mli               #+#    #+#              #
#    Updated: 2020/12/29 18:58:14 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def MakeNpCountUnique(x: np.ndarray) -> dict:
    res = dict(zip(*np.unique(x, return_counts=True)))
    res.setdefault(True, 0)
    res.setdefault(False, 0)
    return res


def confusion_matrix_(y_true: np.ndarray, y_hat: np.ndarray,
                      labels: list = None, df_opt: bool = False) -> np.ndarray:
    """ Compute confusion matrix to evaluate the accuracy of a classification.
    Args:
        y_true: a numpy.ndarray for the correct labels
        y_hat: a numpy.ndarray for the predicted labels
        labels: optional, a list of labels to index the matrix.
            This may be used to reorder or select a subset of labels. (default=None)
    Returns:
        The confusion matrix as a numpy ndarray.
        None on any error.
    Raises:
        This function should not raise any Exception.
    """
    if labels is None:
        labels = np.unique(np.concatenate((y, y_hat)))
    elif not isinstance(labels, np.ndarray):
        labels = np.asarray(labels)
    n = labels.size
    res = np.zeros((n, n), dtype="int64")
    for i in range(n):
        true_is_label = y_true == labels[i]
        for j in range(n):
            res[i][j] = MakeNpCountUnique(true_is_label & (y_hat == labels[j]))[True]
    if df_opt:
        res = pd.DataFrame(res, columns=labels, index=labels)
    return res


if __name__ == "__main__":
    y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'bird'])
    y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet'])

    # Example 1:
    print(confusion_matrix_(y, y_hat))
    #print(confusion_matrix(y, y_hat))
    """
    array([[0 0 0]
           [0 2 1]
           [1 0 2]])
    """

    # Example 2:
    print(confusion_matrix_(y, y_hat, labels=['dog', 'norminet']))
    #print(confusion_matrix(y, y_hat, labels=['dog', 'norminet']))
    """
    array([[2 1]
           [0 2]])
    """

    print("\nInto pandas.DataFrame:")
    print(confusion_matrix_(y, y_hat, df_opt=True))
    print(confusion_matrix_(y, y_hat, labels=['dog', 'norminet'], df_opt=True))
    print(confusion_matrix_(y, y_hat, labels=['bird', 'dog'], df_opt=True))
