from datetime import date
import api_requests as api

meal_category = {1: 'Vegetarian', 2: 'Pasta',
                 3: 'Miscellaneous', 4: 'Goat'}

cocktail_dict = {1: 'Non-Alcoholic', 2: 'Champagne',
                 3: 'Vodka', 4: 'Scotch'}

genres_dict = {1: 'indie', 2: 'soul', 3: 'rock', 4: 'metal'}

trivia_dict = {1: 'soft', 2: 'romantic', 3: 'bold', 4: 'extra bold'}

movies_dict = {1: 'Comedy', 2: 'Romance', 3: 'Action', 4: 'Crime'}


date_type = 0
print('-'*32)
print(f"| WELCOME TO DATING APP PROJECT |")
print('-'*32)
while date_type not in [1, 2, 3, 4]:
    date_type = int(input(
        "\nEnter the type of date you want:\n\n[1] - Soft\n[2] - Romantic\n[3] - Bold\n[4] - Extra bold\n\nYour choice: "))
    print('\n')


music = api.get_playlist(genres_dict[date_type])
