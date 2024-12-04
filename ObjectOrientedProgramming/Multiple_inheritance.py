

# cusine(cusine_name)
# MealType(nzme)
# Dish(dish_name) display_dish_info()


# eg: indian
# break_fast
# gheeroast



class Cusine:

    cusine_name=str

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

    def display_cusine_info(self):

        print(self.cusine_name)    



class MealType:

    name=str

    def __init__(self,name):

        self.name=name

    def display_mealtype_info(self):

        print(self.name)    


class Dish:

    dish_name=str

    def __int__(self,dish_name):

        self.dish_name=dish_name     

    def display_dish_info(self):

        print(self.dish_name)    