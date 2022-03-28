# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 18:45:06 by mli               #+#    #+#              #
#    Updated: 2022/03/29 00:37:36 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from FileLoader import FileLoader

class MyPlotLib:
    @staticmethod
    def histogram(df: pd.DataFrame, features: list) -> None:
        nfeatures = len(features)
        fig, ax = plt.subplots(ncols=nfeatures)
        for i in range(nfeatures):
            ax[i].set_title(features[i])
            ax[i].hist(df[features[i]].dropna())
            ax[i].grid()
        plt.show()

    @staticmethod
    def density(df: pd.DataFrame, features: list) -> None:
        pd.DataFrame(df[features]).plot(kind='density')
        plt.show()

    @ staticmethod
    def pair_plot(df: pd.DataFrame, features: list) -> None:
        pd.plotting.scatter_matrix(df[features])
        plt.show()

    @ staticmethod
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

if __name__ == "__main__":
    main()
