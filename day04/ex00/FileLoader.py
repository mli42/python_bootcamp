# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/29 23:15:06 by mli               #+#    #+#              #
#    Updated: 2022/03/24 23:00:55 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from sys import stderr

class FileLoader:
    @staticmethod
    def load(path: str) -> pd.DataFrame or None:
        df = None
        try:
            df = pd.read_csv(path)
            print("Loading dataset of dimensions %d x %d" %(df.shape[0], df.shape[1]))
        except Exception as e:
            print(f"Exception: {e.__class__.__name__}: {e.strerror if hasattr(e, 'strerror') else e}", file=stderr)
        return df

    @staticmethod
    def display(df: pd.DataFrame, n: int) -> None:
        if not (isinstance(df, pd.DataFrame) and isinstance(n, int)):
            print("Could't display pandas.DataFrame", file=stderr)
            return
        res = df[:n] if (n >= 0) else df[n:]
        print(res)

def main():
    loader = FileLoader()
    def display_dataFrame(path: str) -> None:
        data = loader.load(path)
        loader.display(data, 3)
        print("----------------------------------")
        loader.display(data, 0)
        print("----------------------------------")
        loader.display(data, -3)
        print("----------------------------------")
        print("----------------------------------")

    display_dataFrame("./test.csv")
    display_dataFrame("../resources/test.csv")
    display_dataFrame("../resources/athlete_events.csv")

if __name__ == "__main__":
    main()
