# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/30 01:42:48 by mli               #+#    #+#              #
#    Updated: 2022/03/30 23:58:43 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader

class Komparator:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def __guard(funct):
        def inner(self, categorical_var: str, numerical_var: str) -> None:
            if not isinstance(self.df, pd.DataFrame):
                return None
            columns = self.df.columns.values
            if not (
                all([(isinstance(obj, str) and obj in columns) for obj in [categorical_var, numerical_var]]) and
                self.df[categorical_var].dtype.kind in 'O' and # string
                self.df[numerical_var].dtype.kind in 'iuf' # integer / unsigned / float
            ):
                return None

            return_value = funct(self, categorical_var, numerical_var)
            return return_value
        return (inner)

    @__guard
    def compare_box_plots(self, categorical_var: str, numerical_var: str) -> None:
        df = self.df[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()

        fig, axes = plt.subplots(ncols=len(features))
        for i, feat in enumerate(features):
            axes[i].set_title(feat)
            axes[i].boxplot(df[df[categorical_var] == feat][numerical_var])
        plt.show()

    @__guard
    def density(self, categorical_var: str, numerical_var: str) -> None:
        df = self.df[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()

        fig, axes = plt.subplots(nrows=len(features))
        for i, feat in enumerate(features):
            axes[i].set_title(feat)
            df[df[categorical_var] == feat][numerical_var].plot(kind='density', ax=axes[i], label=numerical_var)
            axes[i].legend()
        fig.tight_layout()
        plt.show()

    @__guard
    def compare_histograms(self, categorical_var: str, numerical_var: str) -> None:
        df = self.df[[categorical_var, numerical_var]].dropna()
        features = df[categorical_var].unique()

        fig, axes = plt.subplots(nrows=len(features))
        for i, feat in enumerate(features):
            axes[i].set_title(feat)
            axes[i].hist(df[df[categorical_var] == feat][numerical_var], label=numerical_var)
            axes[i].legend()
        plt.show()

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    kmp = Komparator(data)

    kmp.compare_box_plots("Sex", "Height")
    kmp.compare_box_plots("Medal", "Age")
    kmp.compare_histograms("Medal", "Height")
    kmp.compare_histograms("Medal", "Age")
    kmp.density("Medal", "Weight")

    print('-' * 10)
    # Won't show anything
    kmp.density("Medal", "Medal")
    kmp.compare_box_plots("Medal", "Medal")
    kmp.compare_histograms("Medal", "Medal")
    kmp.compare_histograms("Height", "Height")

if __name__ == "__main__":
    main()
