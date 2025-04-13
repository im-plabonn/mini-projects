user_input = input("Paste/Write Text Here: ")
character = len(user_input)
words = len(user_input.split())

if words == 1:
    word_label = "word"
else:
    word_label = "words"

if character == 1:
    char_label = "character"
else:
    char_label = "characters"

print(f"{words} {word_label}, {character} {char_label}")
