# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 17:28:13 by mli               #+#    #+#              #
#    Updated: 2020/12/06 17:50:38 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def when(self, location: str) -> list:
        df = self.df[self.df["City"] == location]
        lst = df["Year"].drop_duplicates().to_list()
        return (lst)

    def where(self, date: int) -> list:
        df = self.df[self.df["Year"] == date]
        lst = df["City"].drop_duplicates().to_list()
        return (lst)

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('./resources/athlete_events.csv')

    sp = SpatioTemporalData(data)
    print(sp.where(1896)) # ['Athina']
    print(sp.where(2016)) # ['Rio de Janeiro']
    print(sp.when('Athina')) # [2004, 1906, 1896]
    print(sp.when('Paris')) # [1900, 1924]