# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 18:45:06 by mli               #+#    #+#              #
#    Updated: 2022/03/31 00:39:48 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader

class MyPlotLib:

    def __guard(funct):
        def inner(df: pd.DataFrame, features: list) -> None:
            if not isinstance(df, pd.DataFrame):
                return None
            columns = df.columns.values
            if not (isinstance(features, list) and
                all([(isinstance(obj, str) and (obj in columns) and df[obj].dtype.kind in 'iuf') for obj in features])):
                return None
            return_value = funct(df, features)
            return return_value
        return (inner)

    @staticmethod
    @__guard
    def histogram(df: pd.DataFrame, features: list) -> None:
        nfeatures = len(features)
        fig, ax = plt.subplots(ncols=nfeatures)
        for i in range(nfeatures):
            ax[i].set_title(features[i])
            ax[i].hist(df[features[i]].dropna())
            ax[i].grid()
        plt.show()

    @staticmethod
    @__guard
    def density(df: pd.DataFrame, features: list) -> None:
        pd.DataFrame(df[features]).plot(kind='density')
        plt.show()

    @ staticmethod
    @__guard
    def pair_plot(df: pd.DataFrame, features: list) -> None:
        pd.plotting.scatter_matrix(df[features])
        plt.show()

    @ staticmethod
    @__guard
    def box_plot(df: pd.DataFrame, features: list) -> None:
        nfeatures = len(features)
        fig, ax = plt.subplots()
        ax.boxplot(df[features].dropna(), labels=features)
        plt.show()

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    mpl = MyPlotLib()

    mpl.histogram(data, ["Height", "Weight"])
    mpl.density(data, ["Weight", "Height"])
    mpl.pair_plot(data, ["Weight", "Height"])
    mpl.box_plot(data, ["Weight", "Height"])

    mpl.box_plot(data, ["Weight", "Medal"])

if __name__ == "__main__":
    main()
