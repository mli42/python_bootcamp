# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/08 15:49:03 by mli               #+#    #+#              #
#    Updated: 2020/12/08 16:56:55 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class TinyStatistician:
    @staticmethod
    def mean(x: list) -> float:
        m = len(x)
        if m == 0:
            return None
        return sum(x) / m

    @staticmethod
    def quartile(x: list, percentile: int) -> float:
        m = len(x)
        if m == 0:
            return None
        i = int((percentile / 100) * m)
        x = sorted(x)
        res = x[i]
        if m % 2 == 0:
            res += x[i - 1]
            res /= 2
        return float(res)

    @staticmethod
    def median(x: list) -> float:
        return TinyStatistician.quartile(x, 50)

    @staticmethod
    def var(x: list) -> float:
        m = len(x)
        if m == 0:
            return None
        res = 0
        xmean = TinyStatistician.mean(x)
        for i in range(m):
            res += (x[i] - xmean) ** 2
        return res / m

    @staticmethod
    def std(x: list) -> float:
        return TinyStatistician.var(x) ** 0.5

if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    b = [4, 8, 11, 18, 22, 23, 30, 32]

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
