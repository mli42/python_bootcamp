# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SpatioTemporalData.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 17:28:13 by mli               #+#    #+#              #
#    Updated: 2022/03/31 00:58:14 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def when(self, location: str) -> list:
        if not (isinstance(self.df, pd.DataFrame) and isinstance(location, str)):
            return None
        df = self.df[self.df["City"] == location]
        lst = df["Year"].drop_duplicates().to_list()
        return (lst)

    def where(self, date: int) -> list:
        if not (isinstance(self.df, pd.DataFrame) and isinstance(date, int)):
            return None
        df = self.df[self.df["Year"] == date]
        lst = df["City"].drop_duplicates().to_list()
        return (lst)

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')

    sp = SpatioTemporalData(data)
    print(sp.where(1896)) # ['Athina']
    print(sp.where(2016)) # ['Rio de Janeiro']
    print(sp.when('Athina')) # [2004, 1906, 1896]
    print(sp.when('Paris')) # [1900, 1924]

    print(sp.where(2000)) # ['Sydney']
    print(sp.where(1980)) # ['Lake Placid', 'Moskva']
    print(sp.when('London')) # [2012, 1948, 1908]

    print(sp.where("1980")) # None
    print(sp.when(1980)) # None

if __name__ == "__main__":
    main()
