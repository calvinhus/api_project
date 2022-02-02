# import libraries
import api_requests as our_api
import os
from dotenv import load_dotenv
load_dotenv()

smt = os.environ.get("API_KEY")
print(smt)
print(f"\n\t\t\t---WELCOME TO DATING APP PROJECT---\n")
#duration = input("\nEnter duration: ")
# date_type = input(
#    "\nEnter the type of date you want:\n\nRomantic - [1]\nSoft - [2]\nBold - [3]\nXtra Bold - [4]\n\nYour choice:")

# our_api.get_meal("Vegetarian")
