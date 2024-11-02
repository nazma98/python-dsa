def is_unique_word(word):
    word = word.lower()
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            return False
        letter_count[letter] = 1

    return True


word = "swefi"

if is_unique_word(word):
    print("Unique word!")

else:
    print("Repeated letter!")
