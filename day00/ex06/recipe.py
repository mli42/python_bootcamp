# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 10:13:57 by mli               #+#    #+#              #
#    Updated: 2021/11/21 15:01:40 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Use of nested dictionary

cookbook = {}

def print_recipe(recipe: str) -> None:
    print("Here is your recipe for %s, a %s meal:" %(recipe, cookbook[recipe]["meal"]))
    print("It takes %d minutes of cooking." %(cookbook[recipe]["prep_time"]))
    print("And that's what you'll need : ", end="")
    print(", ".join(cookbook[recipe]["ingredients"]))

def recipe_delone(recipe: str) -> None:
    print("%s's recipe is deleted\n" %recipe)
    del cookbook[recipe]

def addrecipe(recipe: str, t_meal: str, time: int, ingredients: list[str], verbose: bool = True):
    cookbook[recipe] = {"meal" : t_meal, "prep_time" : time, "ingredients" : ingredients}
    if (verbose):
        print("%s's recipe is added\n" %recipe)

def print_cookbook():
    if len(cookbook) == 0:
        print("Your cookbook is empty :(")
    else:
        print("The cookbook contains:")
        for recipe in cookbook:
            print("- " + recipe)
    print("")

# Function used in the loop:

def strip_arr(src: list[str]) -> list[str]:
    for elem in src:
        yield elem.strip()

def ft_addrecipe():
    try:
        recipe_name = str(input("Please, set your recipe name: "))
        type_meal = str(input("and its type of meal: "))
        time_min = int(input("How long does it takes, in minutes: "))
        if (time_min < 0): raise ValueError
        ingredients = str(input("Don't forget the ingredients ! : ")).split(",")
    except ValueError:
        print("\nWrong input...\n")
        return
    ingredients = [elem for elem in strip_arr(ingredients) if (len(elem) > 0)]
    addrecipe(recipe_name, type_meal, time_min, ingredients)

def ft_delrecipe():
    print_cookbook()
    try:
        to_del = str(input("Which recipe do you want to delete ?\nWrite '-1' to giveup: "))
    except ValueError:
        print("\nWrong input... Try again\nSet '-1' to giveup\n")
        ft_delrecipe()
    if (to_del != "-1"):
        recipe_delone(to_del) if (to_del in cookbook) else print("\nError, Not in cookbook\n")

def ft_onerecipe():
    print_cookbook()
    try:
        to_look = str(input("Which recipe do you want to read ? '-1' to giveup: "))
    except ValueError:
        print("\nWrong input... Try again\nSet '-1' to giveup\n")
        ft_onerecipe()
    if (to_look != "-1"):
        print_recipe(to_look) if (to_look in cookbook) else print("\nError, Not in cookbook\n")
    else:
        print("")

def ft_exit():
    print("\n\tHope you found what you were looking for, bye !\n")

# Init the cookbook with 3 recipes:
addrecipe("sandwich", "lunch", 10, ["ham", "bread", "cheese", "tomatoes"], False)
addrecipe("cake", "dessert", 60, ["flour", "suggar", "eggs"], False)
addrecipe("salad", "lunch", 15, ["avocado", "arugula", "tomatoes", "spinach"], False)

# Algorithm

choice = 0
loop_var = {1 : ["Add a recipe", ft_addrecipe],
            2 : ["Delete a recipe", ft_delrecipe],
            3 : ["Print one of your recipes", ft_onerecipe],
            4 : ["Print the cookbook", print_cookbook], 5 : ["Quit", ft_exit]}

while (choice != 5):
    print("Please, select one of these options:")
    for item in loop_var:
        print("%d : %s" %(item, loop_var[item][0]))
    try:
        choice = int(input("\nSo, what's your choice ? : "))
    except ValueError:
        choice = 0
    if (choice > 0 and choice < 6):
        loop_var[choice][1]()
    else:
        print("\nWrong input, try again !\n")
