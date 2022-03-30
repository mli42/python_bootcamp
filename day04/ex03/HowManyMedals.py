# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 16:25:48 by mli               #+#    #+#              #
#    Updated: 2022/03/31 00:54:16 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def howManyMedals(df: pd.DataFrame, name: str) -> dict:
    if not (isinstance(df, pd.DataFrame) and isinstance(name, str)):
        return None
    res = dict()
    df = df[(df["Name"] == name)]
    for index, row in df.iterrows():
        year = row["Year"]
        medal = row["Medal"]
        if year not in res.keys():
            res.update({year: {"G": 0, "S": 0, "B": 0}})
        if medal == "Gold":
            res[year]["G"] += 1
        elif medal == "Silver":
            res[year]["S"] += 1
        elif medal == "Bronze":
            res[year]["B"] += 1
    return (res)

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')

    def test(name, expected):
        mine = howManyMedals(data, name)
        print(mine, "<-- Mine")
        print(expected, "<-- Expected")
        print("Same?", (mine == expected), "\n")

    test("Kjetil Andr Aamodt", {
        1992: {'G': 1, 'S': 0, 'B': 1},
        1994: {'G': 0, 'S': 2, 'B': 1},
        1998: {'G': 0, 'S': 0, 'B': 0},
        2002: {'G': 2, 'S': 0, 'B': 0},
        2006: {'G': 1, 'S': 0, 'B': 0}})
    test('Gary Abraham', {1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}})
    test('Yekaterina Konstantinovna Abramova', {2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}})
    test('Kristin Otto', {1988: {'G': 6, 'S': 0, 'B': 0}})

    test(None, None)

if __name__ == "__main__":
    main()
