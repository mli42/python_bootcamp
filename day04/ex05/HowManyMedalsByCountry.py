# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/30 00:30:29 by mli               #+#    #+#              #
#    Updated: 2022/03/30 01:40:54 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from FileLoader import FileLoader

def howManyMedalsByCountry(df: pd.DataFrame, country: str) -> dict:
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
    team_sports_did = {}

    res = dict()
    df = df[(df["Team"] == country)]
    for index, row in df.iterrows():
        year = row["Year"]
        medal = row["Medal"]
        sport = row["Sport"]
        if year not in res.keys():
            res.update({year: {"G": 0, "S": 0, "B": 0}})
            team_sports_did.update({year: []})
        if sport in team_sports_did[year]:
            pass
        elif medal == "Gold":
            res[year]["G"] += 1
        elif medal == "Silver":
            res[year]["S"] += 1
        elif medal == "Bronze":
            res[year]["B"] += 1
        if (not isinstance(medal, str)) and (sport in team_sports):
            team_sports_did[year].append(sport)
    res = dict(sorted(res.items(), key=lambda x: x[0]))
    return (res)

def main():
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')

    def test(name, expected):
        mine = howManyMedalsByCountry(data, name)
        print(mine, "<-- Mine")
        print(expected, "<-- Expected")
        print("Same?", (mine == expected), "\n")

    test("United States", {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 64, 'S': 67, 'B': 65}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 111, 'S': 45, 'B': 38}, 1924: {'G': 92, 'S': 44, 'B': 50}, 1928: {'G': 37, 'S': 21, 'B': 17}, 1932: {'G': 59, 'S': 56, 'B': 62}, 1936: {'G': 43, 'S': 29, 'B': 27}, 1948: {'G': 69, 'S': 34, 'B': 29}, 1952: {'G': 66, 'S': 38, 'B': 24}, 1956: {'G': 50, 'S': 55, 'B': 20}, 1960: {'G': 93, 'S': 27, 'B': 18}, 1964: {'G': 89, 'S': 36, 'B': 28}, 1968: {'G': 96, 'S': 35, 'B': 34}, 1972: {'G': 69, 'S': 69, 'B': 41}, 1976: {'G': 73, 'S': 53, 'B': 28}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 176, 'S': 96, 'B': 32}, 1988: {'G': 76, 'S': 56, 'B': 44}, 1992: {'G': 88, 'S': 41, 'B': 82}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 143, 'S': 38, 'B': 44}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 126, 'S': 29, 'B': 45}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 105, 'S': 64, 'B': 57}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 94, 'S': 108, 'B': 70}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 119, 'S': 44, 'B': 36}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 115, 'S': 51, 'B': 66}})

if __name__ == "__main__":
    main()
