from gtts import gTTS
from zipfile import ZipFile
import os
import pandas as pd
# ---------------------------- PANDAS ------------------------------- #
foreign_language_to_english_data = pd.read_csv("Polish To English Data - 500.csv")
# print(foreign_language_to_english_data)
foreign_language_to_english_dictionary = foreign_language_to_english_data.to_dict(orient="records")
print(foreign_language_to_english_dictionary)
words_list = [(item["Rank"],item["Polish"]) for item in foreign_language_to_english_dictionary]
print(words_list)

# List of 500 Polish words with rank
words = words_list
print(words_list)

# Create folder to store MP3s
os.makedirs("polish_audio", exist_ok=True)

# Generate MP3 files
for rank, word in words:
    tts = gTTS(text=word, lang='pl')
    filename = f"polish_audio/{rank}_{word}.mp3"
    tts.save(filename)
    print(f"Saved: {filename}")

# # Create ZIP file with all MP3s
# zip_filename = "polish_audio.zip"
# with ZipFile(zip_filename, 'w') as zipf:
#     for rank, word in words:
#         zipf.write(f"polish_audio/{rank}_{word}.mp3")

print("All MP3 files have been generated and zipped into 'polish_audio.zip'.")