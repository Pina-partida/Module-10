class Recipe:
  def __init__(self, name):
    self._name = name
    self._ingredients = [] #starting with an empty list of ingredients 

  def add_ingredient(self, ingredient_name):
    print("Adding ingredient", ingredient_name)
    self._ingredients.append(ingredient_name)

  def remove_ingredient(self, ingredient_name):
    print("Removing ingredient", ingredient_name)
    self._ingredients.remove(ingredient_name)

  def print_ingredients(self):
    print("Ingredients for this recipe are:")
    print(self._ingredients)

#now let's use the above class using this test code
bhel_recipe = Recipe("Bhel") #create an object
bhel_recipe.add_ingredient("Puffed rice") #add an ingredient
bhel_recipe.add_ingredient("Raw onions")
bhel_recipe.add_ingredient("Tomatoes")
bhel_recipe.add_ingredient("Tamarind juice")
bhel_recipe.add_ingredient("Red chilli powder")
bhel_recipe.add_ingredient("Ground Coriander")
bhel_recipe.add_ingredient("Salt")
bhel_recipe.remove_ingredient("Salt") #remove an ingredient
bhel_recipe.print_ingredients() #print the list of ingredients so far
