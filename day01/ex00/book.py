# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 12:30:57 by mli               #+#    #+#              #
#    Updated: 2020/01/15 16:20:04 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:
    creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}

    def __init__(self, name="Cookbook"):
        self.name = name

    def get_recipe_by_name(self, name=None):
        for meal_type in self.recipes_list:
            for meal in self.recipes_list.get(meal_type):
                if (meal == name):
                    return (meal)
        return (None)

    def get_recipes_by_types(self, recipe_type=None):
        meal_names = []
        if (recipe_type in self.recipes_list):
            for meal in self.recipes_list[recipe_type]:
                meal_names.append(meal.name)
        return (meal_names)

    def add_recipe(self, recipe=None):
        if (isinstance(recipe, Recipe)):
            self.recipes_list[recipe.recipe_type].append(recipe)
            last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        else:
            print("Given recipe is not a Recipe")
'''
abc = Book()

salad = Recipe("salad", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
abc.add_recipe(salad)

soupe = Recipe("soupe", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
abc.add_recipe(soupe)

cake = Recipe("cake", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "dessert")
abc.add_recipe(cake)

print("Starter : " + str(abc.get_recipes_by_types('starter')))
print("Lunch : " + str(abc.get_recipes_by_types('lunch')))
print("Dessert : " + str(abc.get_recipes_by_types('dessert')))
'''
