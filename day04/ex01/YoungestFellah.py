# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/02 16:43:22 by mli               #+#    #+#              #
#    Updated: 2020/12/02 22:23:48 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def youngestFellah(df: pd.DataFrame, year: int) -> dict:
    df_that_year = df[df["Year"]==year]
    df_that_year = df_that_year.sort_values(by=["Age"])
    first = df_that_year.iloc[0]
    i = 1
    while df_that_year.iloc[i]["Sex"] == first["Sex"]:
        i += 1
    second = df_that_year.iloc[i]
    return {first["Sex"]: first["Age"], second["Sex"]: second["Age"]}

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    print(youngestFellah(data, 2004)) # {'F': 13.0, 'M': 14.0}
