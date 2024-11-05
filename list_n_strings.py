# List and Strings

#     Given a sentence, split the sentence into words and store each word in a list.
sentence = input("Enter a sentence: ")
words = []
word = ""
for letter in sentence:
    if letter == " ":
        if word: 
            words.append(word)
            word = ""
    else: 
        word += letter

if word:
    words.append(word)

print(words)

#     Sort the words alphabetically.
#     Create a new sentence from the list, with words joined by a comma.