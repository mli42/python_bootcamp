# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 16:25:48 by mli               #+#    #+#              #
#    Updated: 2020/12/06 17:17:35 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def howManyMedals(df: pd.DataFrame, name: str) -> dict:
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

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('./resources/athlete_events.csv')
    mine = howManyMedals(data, "Kjetil Andr Aamodt")
    expected = {1992: {'G': 1, 'S': 0, 'B': 1},
                1994: {'G': 0, 'S': 2, 'B': 1},
                1998: {'G': 0, 'S': 0, 'B': 0},
                2002: {'G': 2, 'S': 0, 'B': 0},
                2006: {'G': 1, 'S': 0, 'B': 0}}
    print("Expected :", expected, sep="\n")
    print("Same ?", (mine == expected))
