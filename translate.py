import os
from google.cloud import translate_v2 as translate

# Set environment variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"  # Replace with the path to your Google Cloud credentials
project_id = "your-project-id"  # Replace with your Google Cloud project ID
source_language = "en"  # Source language (e.g., English)
target_language = "da"  # Target translation language (e.g., Danish)

# Initialize the Translate API client
client = translate.Client()

# Function to translate a string
def translate_string(text):
    translation = client.translate(text, source_language=source_language, target_language=target_language)
    return translation["translatedText"]

# Function to translate a .pot file
def translate_pot_file(pot_file_path):
    with open(pot_file_path, "r", encoding="utf-8") as pot_file:
        pot_content = pot_file.read()

    # Split the .pot content into individual string messages
    single_string_translations = pot_content.split("\n\n")

    translated_pot_content = ""

    for single_string_translation in single_string_translations:
        original_string = single_string_translation.strip()
        translated_string = translate_string(original_string)
        translated_pot_content += f"{translated_string}\n\n"

    # Overwrite the .pot file with the translated string messages
    with open(pot_file_path, "w", encoding="utf-8") as pot_file:
        pot_file.write(translated_pot_content)

# Specify the path to your .pot file
pot_file_path = "path/to/your/theme/languages/your-theme.pot"

# Translate the .pot file
translate_pot_file(pot_file_path)

print("The .pot file has been translated.")
