# import libraries
import requests
import random
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os
from dotenv import load_dotenv
load_dotenv()


def get_meal(category):
    """This method requests all meals from a given category (passed as an input parameter)
        and chooses a random one from the returned dictionary"""
    meals_dict = {}
    category_url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category

    print(category_url)
    response = requests.get(category_url)
    if response.status_code == 200:
        meals_list = list(response.json()['meals'])
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


def get_cocktail(category):
    """Document this method"""
    cocktails_dict = {}

    if category == 'Non-Alcoholic':
        # use the query to filter by non alcoholic drinks
        url = 'http://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic'
    else:
        # use the query to filter by ingredient
        url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + category
    response = requests.get(url)
    # create a list with the dictionaries for all drinks based on the category
    cocktails_list = list(response.json()['drinks'])
    # select a random cocktail
    cocktail = random.choice(cocktails_list)
    # cocktail id
    cocktail_id = cocktail['idDrink']
    # use query to lookup details about the cocktail
    url = 'http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i='+cocktail_id
    response = requests.get(url)
    # cocktail name, cocktail instructions, cocktail image, cocktail video
    cocktail_name = response.json()['drinks'][0]['strDrink']  # name
    cocktail_instructions = response.json(
    )['drinks'][0]['strInstructions']  # instructions
    cocktail_image = response.json()['drinks'][0]['strDrinkThumb']  # image
    cocktail_video = response.json()['drinks'][0]['strVideo']  # video
    # cocktail ingredients
    ingredients_list = []
    for i in range(1, 16):
        ingredient = response.json(
        )['drinks'][0]['strIngredient'+str(i)]  # ingredients
        if ingredient == None:
            break
        else:
            ingredients_list.append(ingredient)

        # build dictionary with all the outputs that we want
        cocktails_dict['Cocktail'] = cocktail_name
        cocktails_dict['Instructions'] = cocktail_instructions
        cocktails_dict['Image'] = cocktail_image
        cocktails_dict['video'] = cocktail_video
        cocktails_dict['Ingredients'] = ingredients_list

    # build final dataframe
    return pd.DataFrame([cocktails_dict])

<<<<<<< HEAD

def get_playlist(category):
    """comment this method"""
    username = os.environ.get("USERNAME")
    scope = os.environ.get("SCOPE")
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    redirect_uri = os.environ.get("REDIRECT_URI")

    token = util.prompt_for_user_token(username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri
                                       )
    endpoint_url = "https://api.spotify.com/v1/recommendations?"

    # OUR FILTERS
    limit = 10
    market = "US"
    seed_genres = category

    query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}'

    bearer = "Bearer " + token
    response = requests.get(query,
                            headers={"Content-Type": "application/json",
                                     "Authorization": bearer})
    json_response = response.json()

    for i in json_response['tracks']:
        print(f"\"{i['name']}\" by {i['artists'][0]['name']}")


def get_trivia(category):
    """Retrieves quotes by category of dating as a conversation starter."""
    try:
        if category == 'soft':
            url = "https://catfact.ninja/fact"
            return requests.get(url).json()['fact']
        elif category == 'romantic':
            url = "https://poetrydb.org/random"
            # requests.get(url).json()[0]['lines']
            return "All you need is love."
        elif category == 'bold':
            url = "https://api.chucknorris.io/jokes/random"
            return requests.get(url).json()['value']
        else:
            url = "http://www.boredapi.com/api/activity/"
            return requests.get(url).json()['activity']
    except:
        print("Sorry. Bad request.")
=======
def get_movies(cat):
    movies=pd.read_csv('data\imdb_top_1000.csv')
    movies_dict = {'romantic': 'Romance',
                       'soft': 'Comedy', 'bold': 'Action', 'Extra bold': 'Crime'}
    # Drop columns we will not use
    movies.drop(columns=['Released_Year','Certificate','Runtime','Overview','Meta_score','Director','Star1','Star2','Star3','Star4','No_of_Votes','Gross'],inplace=True)
    # Filter movies dataframe to keep only the movies with "IMDB_Rating">= 8
    cond=movies['IMDB_Rating']>=8
    movies=movies[cond]
    # Filter movies dataframe based on category
    cond=movies['Genre'].str.contains(movies_dict[cat])
    movies=movies[cond]
    # Select a random movie
    return movies.sample()[['Poster_Link','Series_Title']]
>>>>>>> 0b35fb264e287bf6442fbe3f13e48c52c7c8323a
