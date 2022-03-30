# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/30 01:42:48 by mli               #+#    #+#              #
#    Updated: 2022/03/30 02:01:41 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader

class Komparator:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        ...

    def density(self, categorical_var, numerical_var):
        ...

    def compare_histograms(self, categorical_var, numerical_var):
        ...

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    kmp = Komparator(data)

    kmp.compare_box_plots("Medal", "Age")
    kmp.compare_histograms("Medal", "Height")
    kmp.density("Medal", "Weight")

if __name__ == "__main__":
    main()
