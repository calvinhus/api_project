# import libraries
import requests
import random
import pandas as pd


def get_meal(category):
    """This method requests all meals from a given category (passed as an input parameter)
        and chooses a random one from the returned dictionary"""
    meals_dict = {}
    category_url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    categories = requests.get(category_url)
    if categories.status_code == 200:
        meals_list = list(categories.json()['meals'])
        meal_id = random.choice(meals_list)['idMeal']
    else:
        print("Sorry. Bad request.")
    meal_url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + meal_id
    meals = requests.get(meal_url).json()['meals'][0]
    meals_dict['Meal'] = meals['strMeal']
    meals_dict['Instructions'] = meals['strInstructions']
    meals_dict['Video'] = meals['strYoutube']
    meals_dict['Image'] = meals['strMealThumb']
    ingredients_list = []
    for i in range(1, 21):
        ingredient = meals['strIngredient' + str(i)]
        if ingredient == '':
            break
        else:
            ingredients_list.append(ingredient)
    meals_dict['Ingredients'] = ingredients_list
    return pd.DataFrame.from_dict([meals_dict])
