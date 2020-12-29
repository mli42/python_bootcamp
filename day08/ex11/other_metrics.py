# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    other_metrics.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/28 22:58:14 by mli               #+#    #+#              #
#    Updated: 2020/12/29 17:46:31 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def MakeNpCountUnique(x: np.ndarray) -> dict:
    res = dict(zip(*np.unique(x, return_counts=True)))
    res.setdefault(True, 0)
    res.setdefault(False, 0)
    return res


class ConfusionMatrix():
    def __init__(self, y: np.ndarray, y_hat: np.ndarray, pos_label=1) -> None:
        """
        Args:
            y: the correct labels
            y_hat: the predicted labels
            pos_label: the class on which to report (default=1)
        """
        yyhat_eq = y == y_hat
        yyhat_ne = ~yyhat_eq
        self.tp = MakeNpCountUnique(yyhat_eq & (y_hat == pos_label))[True]
        self.tn = MakeNpCountUnique(yyhat_eq & (y_hat != pos_label))[True]
        self.fp = MakeNpCountUnique(yyhat_ne & (y_hat == pos_label))[True]
        self.fn = MakeNpCountUnique(yyhat_ne & (y     == pos_label))[True]


def accuracy_score_(y: np.ndarray, y_hat: np.ndarray) -> float:
    h = MakeNpCountUnique((y == y_hat))[True]
    res = h / y.size
    return res

def precision_score_(y: np.ndarray, y_hat: np.ndarray, pos_label=1) -> float:
    c_matrix = ConfusionMatrix(y, y_hat, pos_label)
    res = c_matrix.tp / (c_matrix.tp + c_matrix.fp)
    return res

def recall_score_(y: np.ndarray, y_hat: np.ndarray, pos_label=1) -> float:
    c_matrix = ConfusionMatrix(y, y_hat, pos_label)
    res = c_matrix.tp / (c_matrix.tp + c_matrix.fn)
    return res

def f1_score_(y: np.ndarray, y_hat: np.ndarray, pos_label=1) -> float:
    precision = precision_score_(y, y_hat, pos_label)
    recall = recall_score_(y, y_hat, pos_label)
    return (2 * precision * recall) / (precision + recall)


def ft_test(flag: int) -> None:
    if flag ==  1:
        y_hat = np.array([1, 1, 0, 1, 0, 0, 1, 1])
        y = np.array([1, 0, 0, 1, 0, 1, 0, 0])
        label = 1
    elif flag in [2, 3]:
        y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog', 'dog', 'dog'])
        y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet', 'dog', 'norminet'])
        label = "dog" if flag == 2 else "norminet"
    else:
        return
    print(confusion_matrix(y, y_hat))
    """
    if flag & 1:
        # Accuracy: 0.5
        # Precision 0.4
        # Recall: 0.6666666666666666
        # F1-score: 0.5
    if flag & 2:
        # Accuracy 0.625
        # Precision 0.6
        # Recall 0.75
        # F1-score 0.6666666666666665
        label = "dog"
    if flag & 4:
        # Accuracy 0.625
        # Precision 0.6666666666666666
        # Recall 0.5
        # F1-score 0.5714285714285715
        label = "norminet"
    """
    tests = []
    tests.append((accuracy_score_(y, y_hat),                    accuracy_score(y, y_hat)))
    tests.append((precision_score_(y, y_hat, pos_label=label),  precision_score(y, y_hat, pos_label=label)))
    tests.append((recall_score_(y, y_hat, pos_label=label),     recall_score(y, y_hat, pos_label=label)))
    tests.append((f1_score_(y, y_hat, pos_label=label),         f1_score(y, y_hat, pos_label=label)))

    for i, ele in enumerate(tests):
        color = "✅" if (ele[0] == ele[1]) else "🚨"
        if ele[0] is not None:
            print("[%d] %s - %.3f. Expected: %.3f" %(i, color, ele[0], ele[1]))
        else:
            print(f"[%d] %s - {ele[0]} Expected: %.3f" %(i, color, ele[1]))


if __name__ == "__main__":
    ft_test(1)
    ft_test(2)
    ft_test(3)
