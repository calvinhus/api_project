# import libraries
import api_requests as api
import os

# Variable declaration
meal_category = {1: 'Vegetarian', 2: 'Pasta',
                 3: 'Miscellaneous', 4: 'Goat'}

cocktail_dict = {1: 'Non-Alcoholic', 2: 'Champagne',
                 3: 'Vodka', 4: 'Scotch'}
genres_dict = {1: 'indie', 2: 'soul', 3: 'rock', 4: 'metal'}
trivia_dict = {1: 'soft', 2: 'romantic', 3: 'bold', 4: 'extra bold'}


def screen_clear():
    """Simple function to clear the console based on OS and add some new lines"""
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows
        _ = os.system('cls')
    print('\n'*10)


screen_clear()
print('-'*32)
print(f"| WELCOME TO DATING APP PROJECT |")
print('-'*32)
date_type = int(input(
    "\nEnter the type of date you want:\n\n[1] - Soft\n[2] - Romantic\n[3] - Bold\n[4] - Extra bold\n\nYour choice: "))


# print(api.get_meal(meal_category[date_type]))
# print(api.get_cocktail(cocktail_dict[date_type]))
# print(api.get_playlist(genres_dict[date_type]))
# print(api.get_trivia(trivia_dict[date_type]))
