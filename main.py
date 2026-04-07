# ---------------------------- IMPORTS ------------------------------- #
import webbrowser

import pandas as pd
import json
from tkinter import *
import random
# ---------------------------- PANDAS ------------------------------- #
foreign_language_to_english_data = pd.read_csv("Polish To English Data - 500.csv")
# print(foreign_language_to_english_data)
foreign_language_to_english_dictionary = foreign_language_to_english_data.to_dict(orient="records")
print(foreign_language_to_english_dictionary)
# foreign_language_to_english_dictionary_converted = {index+1:value for index, value in enumerate(foreign_language_to_english_dictionary)}
# print(foreign_language_to_english_dictionary_converted)
# # print(foreign_language_to_english_dictionary)
# # convert to .json file
# with open('foreign_language_to_english_dictionary.json', 'w') as foreign_language_to_english_dictionary_json_file:
#     json.dump(foreign_language_to_english_dictionary_converted, foreign_language_to_english_dictionary_json_file)
# # read the .json file
# with open('foreign_language_to_english_dictionary.json', 'r') as foreign_language_to_english_dictionary_json_file:
#     json_data = json.load(foreign_language_to_english_dictionary_json_file)
#     # print(json_data)
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
FONT_SIZE = 40
FONT_STYLE = "italic"
FONT_PACK =(FONT, FONT_SIZE, FONT_STYLE)
FONT_COLOR = "black"
TEXT_START_Y = 150
# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
def get_card():
    random_card = random.choice(foreign_language_to_english_dictionary)
    foreign_language_word  = random_card["Polish"]
    foreign_language_word_rank = random_card["Rank"]
    foreign_language_word_english = random_card["English"]
    foreign_language_word_phonetic_pronunciation = random_card["Hint"]
    foreign_language_word_pronunciation_link = random_card["Pronunciation Link"]
    # print(foreign_language_word_rank)
    # print(foreign_language_word)
    # print(foreign_language_word_phonetic_pronunciation)
    # print(foreign_language_word_pronunciation_link)
    # print(foreign_language_word_english)
    canvas.itemconfig(foreign_language_word_placeholder, text=foreign_language_word)
    # canvas.itemconfig(foreign_language_word_english_placeholder, text=foreign_language_word_english)
    canvas.itemconfig(rank_place_holder, text=foreign_language_word_rank)
    canvas.itemconfig(phonetic_word_placeholder, text=foreign_language_word_phonetic_pronunciation)
    canvas.itemconfig(pronunciation_link_placeholder, text=foreign_language_word_pronunciation_link)
    # Create a hyperlink to the pronunciation online
    canvas.tag_bind(pronunciation_link_placeholder, "<Button-1>", lambda event: open_url(foreign_language_word_pronunciation_link))

def open_url(url):
    """Opens a website in the default browser."""
    webbrowser.open(url)
# ---------------------------- UI SETUP ------------------------------- #
# Initialize the window
window = Tk()
window.title(f"Polish to English Practice")
# Padding to the window
window.config( padx=50, pady=50, bg=BACKGROUND_COLOR)
# Canvas for Flash Card
canvas = Canvas(window, width=800, height=526, highlightthickness=0)
front_card_png = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_png)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Text
# Language Title
language_title = canvas.create_text(400, TEXT_START_Y, text="Polish", font=FONT_PACK, fill=FONT_COLOR)
# Foreign Language Word Placeholder
foreign_language_word_placeholder = canvas.create_text(400, TEXT_START_Y+50, text="Polish Word", font=FONT_PACK, fill=FONT_COLOR)
# Phonetic Word Placeholder
phonetic_word_placeholder = canvas.create_text(400, TEXT_START_Y+100, text="English Phonetic Pronunciation", font=FONT_PACK, fill=FONT_COLOR)
# Pronunciation Link Placeholder add a tag so a click event can open a new web page to a hyperlink pronunciation
pronunciation_link_placeholder = canvas.create_text(400, TEXT_START_Y+150, text="Pronunciation Link", font=FONT_PACK, fill="blue", tags="link")
# Rank Placeholder
rank_place_holder = canvas.create_text(400, TEXT_START_Y + 200, text="Rank", font=FONT_PACK, fill=FONT_COLOR)


# English Word Placeholder
# english_word_text = canvas.create_text(400, 200, text="English", font=FONT_PACK, fill=FONT_COLOR)

# Buttons
wrong_png = PhotoImage(file="images/wrong.png")
right_png = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_png, highlightthickness=0, command= lambda: get_card())
right_button = Button(image=right_png, highlightthickness=0, command= lambda: get_card())
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)


# Keep window object open so it doesn't close
window.mainloop()