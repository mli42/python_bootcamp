# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 12:30:57 by mli               #+#    #+#              #
#    Updated: 2021/11/27 23:22:48 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:
    @staticmethod
    def get_current_time() -> str:
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")

    def __init__(self, name="Cookbook"):
        self.name = name
        self.creation_date = self.get_current_time()
        self.last_update = self.creation_date
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}

    def get_recipe_by_name(self, name: str) -> Recipe:
        """Print a recipe with the name `name` and return the instance"""
        for meals in self.recipes_list.values():
            for meal in meals:
                if (meal.name == name):
                    #print(str(meal))
                    return (meal)
        return (None)

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.recipes_list.keys():
            print("Recipe type does not belong to the book")
            return (None)
        meal_names = [meal.name for meal in self.recipes_list[recipe_type]]
        return (meal_names)

    def add_recipe(self, recipe: Recipe) -> None:
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Given recipe is not a Recipe")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = self.get_current_time()

if __name__ == "__main__":
    abc = Book()

    salad = Recipe("salad", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
    abc.add_recipe(salad)

    soupe = Recipe("soupe", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
    abc.add_recipe(soupe)

    cake = Recipe("cake", 1 , 123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "dessert")
    abc.add_recipe(cake)

    print("Get salad : " + str(abc.get_recipe_by_name("salad")))
    print("Starter : " + str(abc.get_recipes_by_types('starter')))
    print("Lunch : " + str(abc.get_recipes_by_types('lunch')))
    print("Dessert : " + str(abc.get_recipes_by_types('dessert')))
