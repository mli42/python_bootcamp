# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/03 18:58:21 by mli               #+#    #+#              #
#    Updated: 2022/03/31 00:51:18 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def proportionBySport(df: pd.DataFrame, yr: int, sport: str, gdr: str) -> float:
    """
        The function answers questions like the following :
            “What was the percentage of female basketball players among all
            the female participants of the 2016 Olympics?”
    Returns:
        float: Percentage of participants who played the given sport among
               the participants of the given gender.
    """
    if not (isinstance(df, pd.DataFrame) and isinstance(yr, int) and
        isinstance(sport, str) and gdr in ['F', 'M']):
        return None
    df = df[(df["Year"]==yr) & (df["Sex"]==gdr)]
    # df = df[~df.duplicated(subset=["ID"])]
    df_res = df[df["Sport"]==sport]
    return (df_res.shape[0] / df.shape[0])

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')

    def test(year, sport, gender, expected):
        print(proportionBySport(data, year, sport, gender))
        print(expected, " <-- Expected\n")

    test(2004, 'Tennis', 'F', "0.02307")
    test(2008, 'Hockey', 'F', "0.03284")
    test(1964, 'Biathlon', 'M', "0.00659")

    test(1964, 'Biathlon', 'G', "None")

if __name__ == "__main__":
    main()
