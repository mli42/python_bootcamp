# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/03 18:58:21 by mli               #+#    #+#              #
#    Updated: 2020/12/04 00:43:58 by mli              ###   ########.fr        #
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
    df = df[(df["Year"]==yr) & (df["Sex"]==gdr)]
    df = df[~df.duplicated(subset=["ID"])]
    df_res = df[df["Sport"]==sport]
    return (df_res.shape[0] / df.shape[0])

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('./resources/athlete_events.csv')
    print(proportionBySport(data, 2004, 'Tennis', 'F')) # 0.01935634328358209
    print(0.01935634328358209)
    # But Conda Python 3.7.4 gives me: 0.019302325581395347
