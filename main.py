# ---------------------------- IMPORTS ------------------------------- #
import pandas as pd
import json
# ---------------------------- PANDAS ------------------------------- #
polish_to_english_data = pd.read_csv("Polish To English Data - 500.csv")
# print(polish_to_english_data)
polish_to_english_dictionary = polish_to_english_data.to_dict(orient="records")
# print(polish_to_english_dictionary)
# convert to .json file
with open('polish_to_english_dictionary.json', 'w') as polish_to_english_dictionary_json_file:
    json.dump(polish_to_english_dictionary, polish_to_english_dictionary_json_file)
# read the .json file
with open('polish_to_english_dictionary.json', 'r') as polish_to_english_dictionary_json_file:
    json_data = json.load(polish_to_english_dictionary_json_file)
    print(json_data)
# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
