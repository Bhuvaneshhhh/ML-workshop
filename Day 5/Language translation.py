from translate import Translator
if __name__ == '__main__':
    pass
from translate import Translator

def translate_text(text, target_language='en'):
    translator = Translator(to_lang = target_language)
    translated_text = translator.translate(text)
    return translated_text

if __name__ == '__main__':
    input_text = input("Enter the text to translate: ")
    target_language = input("Enter the target language: ")
    translated_text = translate_text(input_text, target_language)
    print("Translated text is: ", translated_text)
