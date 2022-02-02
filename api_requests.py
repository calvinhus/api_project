import pandas as pd
import requests
import random


def get_cocktail(cat):
    ingredient_dict={'romantic':'champagne', 'soft': 'Non_Alcoholic', 'bold':'Vodka','Extra bold':'Scotch'}
    if cat == 'soft':
        # use the query to filter by non alcoholic drinks
        url='http://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic'
    else:
        # use the query to filter by ingredient
        url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i='+ingredient_dict[cat]
    response=requests.get(url)    
    # create a list with the dictionaries for all drinks based on the category
    cocktails_list=list(response.json()['drinks'])
    # select a random cocktail
    cocktail=random.choice(cocktails_list)
    # cocktail id
    cocktail_id=cocktail['idDrink']
    # use query to lookup details about the cocktail
    url = 'http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i='+cocktail_id
    response=requests.get(url)
    # cocktail name, cocktail instructions, cocktail image, cocktail video
    cocktail_name=response.json()['drinks'][0]['strDrink'] # name
    cocktail_instructions=response.json()['drinks'][0]['strInstructions'] # instructions
    cocktail_image=response.json()['drinks'][0]['strDrinkThumb'] # image
    cocktail_video=response.json()['drinks'][0]['strVideo'] # video
    # cocktail ingredients
    ingredients_list=[]
    for i in range(1,16):
        ingredient=response.json()['drinks'][0]['strIngredient'+str(i)] # ingredients
        if ingredient==None:
            break
        else:
            ingredients_list.append(ingredient)

        # build dictionary with all the outputs that we want
        cocktails_dict={}
        cocktails_dict['Cocktail']=cocktail_name
        cocktails_dict['Instructions']=cocktail_instructions
        cocktails_dict['Image']=cocktail_image
        cocktails_dict['video']=cocktail_video
        cocktails_dict['Ingredients']=ingredients_list

    # build final dataframe
    return pd.DataFrame([cocktails_dict])
               