# import libraries
import pandas as pd
import api_requests as our_api

print(f"WELCOME TO DATING APP PROJECT")
#duration = input("enter duration: ")
#date_type = input("enter type: ")
movies = pd.read_csv('data/imdb_top_1000.csv')
print(movies['Genre'].unique())
