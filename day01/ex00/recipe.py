# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 09:54:03 by mli               #+#    #+#              #
#    Updated: 2020/01/15 15:41:18 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:

    def __init__(self, name=None, cook_lv=None, cook_time=None, ingr=None, descrip=None, recipe_type=None):
        if (name == None or cook_lv == None or cook_time == None or ingr == None or recipe_type == None):
            print("Null argument not expected")
            exit()
        try:
            name = str(name)
            cook_lv = int(cook_lv)
            cook_time = int(cook_time)
            ingr = list(ingr)
            descrip = str(descrip)
            recipe_type = str(recipe_type)
        except ValueError:
            print("Wrong format of argument")
            exit()
        if (recipe_type != 'lunch' and recipe_type != 'starter' and recipe_type != 'dessert'):
            print("Recipe type not correct, choose 'starter' or 'lunch' or 'dessert'")
            exit()
        if (cook_lv > 5 or cook_lv < 1):
            print("Cooking level is not between 1 and 5")
            exit()
        if (cook_time < 0):
            print("Moron ! Time is not negative...")
            exit()
        self.name = name
        self.cooking_lvl = cook_lv
        self.cooking_time = cook_time
        self.ingredients = ingr
        self.description = descrip
        self.recipe_type = recipe_type

    def __str__(self):
        difficulty = [None, "not ", "not really ", "not too ", "a bit ", ""]
        txt = """That's your %s's recipe details:\n
        \rIt takes %d minutes, and it's %sdifficult.
        \rFor your %s, you will need : %s""" \
        %(self.name, self.cooking_time, difficulty[self.cooking_lvl], self.recipe_type, str(self.ingredients)[1 : -1])
        if (self.description != None):
            txt += "\n\nOh and here is a description of your meal!\n%s" %(self.description)
        return (txt)

#hey = Recipe("salad", 1 , -123, ["Salad of course", "Tomatoes" , "Avocado"], "A meal we can eat", "lunch")
#print(hey)
