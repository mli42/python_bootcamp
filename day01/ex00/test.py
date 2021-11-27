# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/16 21:49:03 by mli               #+#    #+#              #
#    Updated: 2021/11/27 23:22:11 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe
from time import sleep

if __name__ == "__main__":
    cookbook = Book()
    printCounter = 0

    def printLastUpdate():
        global printCounter
        print(f"[{printCounter}] Last update:", cookbook.last_update)
        printCounter += 1

    """These recipes will raise exception"""
    #recipe = Recipe("", 1 , 123, ["Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
    #recipe = Recipe("recipe", 1 , -123, ["Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
    #recipe = Recipe("recipe", 1 , 123, [], "A meal we can eat", "lunch")
    #recipe = Recipe("recipe", 1 , 123, ["something"], "A meal we can eat", "gouter")

    printLastUpdate()
    sleep(0.5)
    printLastUpdate()
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

    printLastUpdate()
    sleep(0.5)
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
    print("___________________________________________________________________")
    printLastUpdate()
