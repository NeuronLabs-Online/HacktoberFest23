from googletrans import Translator, LANGUAGES

def main():
    # Initialize the translator
    translator = Translator()

    print("Supported Languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

    source_lang = input("Enter the source language code (e.g., en for English): ")
    target_lang = input("Enter the target language code (e.g., fr for French): ")
    text_to_translate = input("Enter the text to translate: ")

    try:
        # Translate the text
        translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang)

        # Display the translation
        print(f"Translated text: {translated_text.text}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
