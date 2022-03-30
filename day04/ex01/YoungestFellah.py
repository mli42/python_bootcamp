# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/02 16:43:22 by mli               #+#    #+#              #
#    Updated: 2022/03/31 00:47:27 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from numpy import NaN
from FileLoader import FileLoader

def youngestFellah(df: pd.DataFrame, year: int) -> dict:
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    default_res = { 'F': NaN, 'M': NaN }

    if not (isinstance(df, pd.DataFrame) and isinstance(year, int)):
        return default_res
    df = df[df["Year"]==year].loc[:, ["Sex", "Age"]].sort_values(by=["Age"])
    if len(df) == 0:
        return default_res
    first = df.iloc[0]

    df_second_sex = df.loc[lambda x: x["Sex"] != first["Sex"]]
    second_age = df_second_sex.iloc[0]["Age"] if len(df_second_sex) != 0 else NaN
    second_sex = 'F' if first["Sex"] == 'M' else 'M'
    return dict(sorted(
        { first["Sex"]: first["Age"], second_sex: second_age }.items(),
        key=lambda x: x[0]
    ))

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    print(youngestFellah(data, 1992)) # {'F': 12.0, 'M': 11.0}
    print(youngestFellah(data, 2004)) # {'F': 13.0, 'M': 14.0}
    print(youngestFellah(data, 2010)) # {'F': 15.0, 'M': 15.0}

    print(youngestFellah(data, 1991)) # {'F': NaN, 'M': NaN}
    print(youngestFellah(data, 2003)) # {'F': NaN, 'M': NaN}

    print(youngestFellah(data, "1992")) # {'F': NaN, 'M': NaN}

if __name__ == "__main__":
    main()
