# ---------------------------- IMPORTS ------------------------------- #
import webbrowser
import pandas as pd
from tkinter import *
import random
import pygame
# ---------------------------- PANDAS ------------------------------- #
foreign_language_to_english_data = pd.read_csv("Polish To English Data - 500.csv")
# print(foreign_language_to_english_data)
foreign_language_to_english_dictionary = foreign_language_to_english_data.to_dict(orient="records")
print(foreign_language_to_english_dictionary)
words_list = [(item["Rank"],item["Polish"]) for item in foreign_language_to_english_dictionary][0:25]
print(words_list)
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
FONT_SIZE = 50
FONT_STYLE = "italic"
FONT_PACK =(FONT, FONT_SIZE, FONT_STYLE)
FONT_COLOR = "black"
TEXT_START_Y = 150
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
# Set to empty dict for type
random_card = {}
global is_on
is_on = True

# ---------------------------- FUNCTIONS ------------------------------- #
def get_card():

    global random_card
    # Replace card text fields
    random_card = random.choice(foreign_language_to_english_dictionary)
    foreign_language_word  = random_card["Polish"]
    foreign_language_word_rank = random_card["Rank"]
    foreign_language_word_phonetic_pronunciation = random_card["Hint"]
    # Text Fields State
    canvas.itemconfig(flash_card, image=front_card_png)
    canvas.itemconfig(language_title, text="Polish", fill="black")
    canvas.itemconfig(foreign_language_word_placeholder, text=foreign_language_word, fill="black")
    canvas.itemconfig(rank_place_holder, text=foreign_language_word_rank, fill="black")
    canvas.itemconfig(phonetic_word_placeholder, text=foreign_language_word_phonetic_pronunciation, fill="black")
    # Button State
    wrong_button.config(state="normal")
    play_button.config(command=lambda: play_audio_clip(foreign_language_word_rank, foreign_language_word), state="normal")
    rotate_button.config(state="normal")

def flip_card():
    global is_on
    # Switch card text fields
    if is_on:
        # Text
        # Language Title
        canvas.itemconfig(language_title, text="English", fill="white")
        # Foreign Language Word Placeholder
        canvas.itemconfig(foreign_language_word_placeholder, text="")
        # Phonetic Word Placeholder
        canvas.itemconfig(phonetic_word_placeholder, text=random_card["English"] , fill="white")
        # Rank Placeholder
        canvas.itemconfig(rank_place_holder,text="")
        # Image
        canvas.itemconfig(flash_card, image=back_card_png)
        is_on = False
    else:
        foreign_language_word = random_card["Polish"]
        foreign_language_word_rank = random_card["Rank"]
        foreign_language_word_phonetic_pronunciation = random_card["Hint"]
        canvas.itemconfig(flash_card, image=front_card_png)
        canvas.itemconfig(language_title, text="Polish", fill="black")
        canvas.itemconfig(foreign_language_word_placeholder, text=foreign_language_word, fill="black")
        canvas.itemconfig(rank_place_holder, text=foreign_language_word_rank, fill="black")
        canvas.itemconfig(phonetic_word_placeholder, text=foreign_language_word_phonetic_pronunciation, fill="black")
        play_button.config(command=lambda: play_audio_clip(foreign_language_word_rank, foreign_language_word))
        is_on = True

def open_url(url):
    """Opens a website in the default browser."""
    webbrowser.open(url)
def play_audio_clip(foreign_language_word_rank, foreign_language_word):
    relative_file_path = f"polish_audio/{foreign_language_word_rank}_{foreign_language_word}.mp3"
    # print(relative_file_path)
    # Pygame audio player
    pygame.mixer.init()
    pygame.mixer.music.load(relative_file_path)
    pygame.mixer.music.play(loops=0)
# ---------------------------- UI SETUP ------------------------------- #
# Initialize the window
window = Tk()
window.title(f"Polish to English Practice")
# Padding to the window
window.config( padx=50, pady=50, bg=BACKGROUND_COLOR)
# Canvas for Flash Card
canvas = Canvas(window, width=800, height=526, highlightthickness=0)
front_card_png = PhotoImage(file="images/card_front.png")
back_card_png = PhotoImage(file="images/card_back.png")
flash_card = canvas.create_image(400, 263, image=front_card_png)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=4)

# Text
# Language Title
language_title = canvas.create_text(400, TEXT_START_Y, text="Polish", font=FONT_PACK, fill=FONT_COLOR)
# Foreign Language Word Placeholder
foreign_language_word_placeholder = canvas.create_text(400, TEXT_START_Y+70, text="Polish Word", font=FONT_PACK, fill=FONT_COLOR)
# Phonetic Word Placeholder
phonetic_word_placeholder = canvas.create_text(400, TEXT_START_Y+140, text="English Phonetic Pronunciation", font=FONT_PACK, fill=FONT_COLOR)
# Rank Placeholder
rank_place_holder = canvas.create_text(400, TEXT_START_Y + 210, text="Rank", font=FONT_PACK, fill=FONT_COLOR)
# English Word Placeholder
# english_word_text = canvas.create_text(400, 200, text="English", font=FONT_PACK, fill=FONT_COLOR)

# Buttons
wrong_png = PhotoImage(file="images/wrong.png")
play_png = PhotoImage(file="images/play.png")
rotate_png = PhotoImage(file="images/rotate.png")
right_png = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_png, highlightthickness=0, command= lambda: get_card() ,bd=0, state="disabled")
right_button = Button(image=right_png, highlightthickness=0, command= lambda: get_card() ,bd=0)
rotate_button = Button(image=rotate_png, highlightthickness=0, command=lambda: flip_card() ,bd=0, state="disabled")
play_button = Button(image=play_png, highlightthickness=0, bd=0, state="disabled")

wrong_button.grid(row=1, column=0)
play_button.grid(row=1, column=1)
rotate_button.grid(row=1, column=2)
right_button.grid(row=1, column=3)

wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
rotate_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
play_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)


# Keep window object open so it doesn't close
window.mainloop()