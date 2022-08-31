from translate import Translator

translator = Translator(to_lang="fr")

# translation = translator.translate("There are too many people in the bedroom")

# print(translation)


# To translate other files

try:
    with open('text.txt', mode='r') as tr_file:
        text = tr_file.read()
        translation = translator.translate(text)
        print(translation)
    with open('./text-fr.txt', mode="w") as trld_file:
        trld_file.write(translation)

except FileNotFoundError as err:
    print("Check file path")
    raise err
