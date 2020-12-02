# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/29 23:15:06 by mli               #+#    #+#              #
#    Updated: 2020/11/29 23:38:36 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

class FileLoader:
    @staticmethod
    def load(path: str) -> pd.DataFrame:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions %d x %d" %(df.shape[0], df.shape[1]))
        return df

    @staticmethod
    def display(df: pd.DataFrame, n: int) -> None:
        res = df[:n] if (n >= 0) else df[n:]
        print(res)

if __name__ == "__main__":
    loader = FileLoader()
    #data = loader.load("../resources/test.csv")
    data = loader.load("../resources/athlete_events.csv")
    loader.display(data, 3)
    print("----------------------------------")
    loader.display(data, -3)
