# shimul translator is a translator which converts any vowels in a sentence
# to s
# for example : Cat -> Cst, neko -> nsks

def translate(phrase):
    translation = ""
    vowels=['a', 'e', 'i', 'o', 'u']

    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation += 'S'
            else:
                translation += 's'
        else:
            translation += letter
    return translation

phrase = input("Enter the phrase: ")
# print(phrase) 

print(translate(phrase))




