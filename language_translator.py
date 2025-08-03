# pip install deep-translator

from deep_translator import GoogleTranslator

print("Welcome to the Language Translator!")

# Get input from user
text = input("Enter text to translate: ")
target_lang = input("Enter target language code (e.g., hi = Hindi, es = Spanish, fr = French): ")

try:
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    print("Translated text:", translated)
except Exception as e:
    print("Error:", e)
