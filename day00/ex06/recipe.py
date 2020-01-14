# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 10:13:57 by mli               #+#    #+#              #
#    Updated: 2020/01/14 14:25:09 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Use of nested dictionary

# Init the cookbook with 3 recipes:
cookbook = {}
cookbook["sandwich"] = {"meal" : "lunch", "prep_time" : 10,
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"]}
cookbook["cake"] = {"meal" : "dessert", "prep_time" : 60,
        "ingredients" : ["flour", "suggar", "eggs"]}
cookbook["salad"] = {"meal" : "lunch", "prep_time" : 15,
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"]}

def print_recipe(recipe):
    print("Here is your recipe for %s, a %s meal:" %(recipe, cookbook[recipe]["meal"]))
    print("It takes %d minutes of cooking." %(cookbook[recipe]["prep_time"]))
    print("And that's what you'll need :", cookbook[recipe]["ingredients"])
    print("")

def recipe_delone(recipe):
    print("%s's recipe is deleted\n" %recipe)
    del cookbook[recipe]

def addrecipe(recipe, t_meal, time, ingredients):
    cookbook[recipe] = {"meal" : t_meal, "prep_time" : time, "ingredients" : ingredients}
    print("%s's recipe is added\n" %recipe)

def print_cookbook():
    print("The cookbook contains:")
    for recipe in cookbook:
        print("- " + recipe)
    print("")

# Function used in the loop:

def ft_addrecipe():
    var = []
    try:
        var.append(str(input("Please, set your recipe name: ")))
        var.append(str(input("and its type of meal: ")))
        var.append(int(input("How long does it takes, in minutes: ")))
        var.append(list(input("Don't forget the ingredients ! : ")))
    except ValueError:
        print("\nWrong input... Try again\nSet '-1' in time to giveup\n")
        ft_addrecipe()
    if (var[2] != -1):
        addrecipe(var[0], var[1], var[2], var[3])

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
