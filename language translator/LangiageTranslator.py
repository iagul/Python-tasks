from deep_translator import GoogleTranslator

def translate_text(text, source_lang='auto', target_lang='fr'):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)

text = input("Enter the text to translate: ")

target_lang = input("Enter target language (e.g., 'fr' for French, 'es' for Spanish, 'de' for German): ").lower()

source_lang = 'auto'

translated_text = translate_text(text, source_lang=source_lang, target_lang=target_lang)

print(f"Translated Text ({target_lang}): {translated_text}")
