# Created 7/15/2022
# Purpose of code is to translate text from file into another language

from translate import Translator

translator = Translator(to_lang="ko")

try:
    with open('./translate_text.txt', mode="r") as my_file:
        translation = translator.translate(my_file.read())
        print(translation)
        with open('./translated_text.txt', mode="w") as new_file:
            new_file.write(translation)
except FileNotFoundError as e:
    print("check your file path silly!")