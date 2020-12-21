# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    z-score.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/21 18:30:08 by mli               #+#    #+#              #
#    Updated: 2020/12/21 20:42:43 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class TinyStatistician:
    @staticmethod
    def mean(x: np.ndarray) -> float:
        m = x.size
        if m == 0:
            return None
        return np.sum(x) / m

    @staticmethod
    def quartile(x: np.ndarray, percentile: int) -> float:
        m = x.size
        if m == 0:
            return None
        i = int((percentile / 100) * m)
        x = sorted(x.flatten())
        res = x[i]
        if m % 2 == 0:
            res += x[i - 1]
            res /= 2
        return float(res)

    @staticmethod
    def median(x: np.ndarray) -> float:
        return TinyStatistician.quartile(x, 50)

    @staticmethod
    def var(x: np.ndarray) -> float:
        m = x.size
        if m == 0:
            return None
        x = x.flatten()
        res = 0
        xmean = TinyStatistician.mean(x)
        for i in range(m):
            res += (x[i] - xmean) ** 2
        return res / m

    @staticmethod
    def std(x: np.ndarray) -> float:
        return TinyStatistician.var(x) ** 0.5

if False:
    tstat = TinyStatistician()
    a = np.array([1, 42, 300, 10, 59])
    b = np.array([4, 8, 11, 18, 22, 23, 30, 32])
    """
    a = a.reshape(-1, 1)
    b = b.reshape(-1, 1)
    """

    tests = [[tstat.mean(a),            82.4],
             [tstat.median(a),          42.0],
             [tstat.median(b[:-1]),     18],
             [tstat.median(b),          20],
             [tstat.quartile(a, 25),    10.0],
             [tstat.quartile(a, 75),    59.0],
             [tstat.var(a),             12279.439999999999],
             [tstat.std(a),             110.81263465868862]]

    for i, ele in enumerate(tests):
        color = "✅" if (ele[0] == ele[1]) else "🚨"
        print("[%d] %s - %f. Expected: %f" %(i, color, ele[0], ele[1]))

def zscore(x: np.ndarray) -> np.ndarray:
    """Computes the normalized version of a non-empty numpy.ndarray using the z-score
        standardization.
    Args:
        x: has to be an numpy.ndarray, a vector.
    Returns:
        x' as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function shouldn't raise any Exception.
    """
    mean = TinyStatistician.mean(x)
    std = TinyStatistician.std(x)
    res = np.zeros(x.shape)
    for i in range(x.size):
        res[i] = (x[i] - mean) / std
    return res

if __name__ == "__main__":
    # Example 1:
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    #X = X.reshape(-1, 1)
    print(zscore(X))
    # Output:
    """
    array([-0.08620324,  1.2068453, -0.86203236,  0.51721942,
           0.94823559, 0.17240647, -1.89647119])
    """
    # Example 2:
    X = np.array([2, 14, -13, 5, 12, 4, -19])
    X = X.reshape(-1, 1)
    print(zscore(X))
    # Output:
    """
    array([ 0.11267619,  1.16432067, -1.20187941,  0.37558731,
            0.98904659, 0.28795027, -1.72770165])
    """
