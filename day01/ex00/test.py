# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/16 21:49:03 by mli               #+#    #+#              #
#    Updated: 2020/11/16 22:24:15 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

if __name__ == "__main__":
    cookbook = Book()

    """These recipe's will raise exception"""
    #recipe = Recipe("", 1 , 123, ["Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
    #recipe = Recipe("recipe", 1 , -123, ["Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
    #recipe = Recipe("recipe", 1 , 123, [], "A meal we can eat", "lunch")
    #recipe = Recipe("recipe", 1 , 123, ["something"], "A meal we can eat", "gouter")

    """Test the Book class"""
    recipe = None
    cookbook.add_recipe(recipe)

    recipe = Recipe("myFirstRecipe", 1, 123, ["patience"], "", "lunch")
    cookbook.add_recipe(recipe)

    recipe = Recipe("salad", 1, 10, ["Salad of course", "Tomatoes", "Avocado"],
                    "Small but tasty salad", "starter")
    cookbook.add_recipe(recipe)
    recipe = Recipe("soupe", 2, 40, ["what you want", "Salt"],
                    "The best sips you ever sipped", "lunch")
    cookbook.add_recipe(recipe)

    recipe = Recipe("cake", 3, 120, ["Flour", "Eggs", "Oven"], "Delicious cake", "dessert")
    cookbook.add_recipe(recipe)
    recipe = Recipe("cake2", 5, 180, ["Flour", "Eggs", "Secret things"],
                    "Delicious but damn hard cake", "dessert")
    cookbook.add_recipe(recipe)

    print("___________________________________________________________________")
    print("Get firstRecipe : " + str(cookbook.get_recipe_by_name("myFirstRecipe")))
    print("___________________________________________________________________")
    print("Get salad : " + str(cookbook.get_recipe_by_name("salad")))
    print("___________________________________________________________________")
    print("Get soupe : " + str(cookbook.get_recipe_by_name("soupe")))
    print("___________________________________________________________________")
    print("Get cake : " + str(cookbook.get_recipe_by_name("cake")))
    print("___________________________________________________________________")
    print("Get cake2 : " + str(cookbook.get_recipe_by_name("cake2")))
    print("___________________________________________________________________")
    print("___________________________________________________________________")
    print("Starter : " + str(cookbook.get_recipes_by_types('starter')))
    print("Lunch : " + str(cookbook.get_recipes_by_types('lunch')))
    print("Dessert : " + str(cookbook.get_recipes_by_types('dessert')))
