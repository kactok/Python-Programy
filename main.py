# Morse code wiki: https://en.wikipedia.org/wiki/Morse_code
# Program that converts any String input into Morse Code
# 26 basic Latin letters(a to z) + Arabic numbers
# There is no distinction between upper and loser case letters
# morse code is included in morsecode.py as a dictionary
# Output:
# - words displayed as combination of '-' and '.' (one word is a list of letters)
# - space between letters as '...' - 3 dots
# - space between words as '.......' - 7 dots

from morsecode import morse_code as data

# dict that stores a morse code values of letters/numbers
morse_code_dict = data


def convert(list_of_words: []) -> []:
    """converts a list of words into morse code"""
    morse_code_list = []
    for word in list_of_words:
        new_word = []
        for letter in word:
            letter_as_mc = morse_code_dict.get(letter)
            new_word.append(letter_as_mc)
        morse_code_list.append(new_word)
    return morse_code_list


# User input (all letters lowered)
user_sentence = input('Enter the sentence to be converted into morse code: ').lower()
sentence_as_list = user_sentence.split()
print(sentence_as_list)
output = convert(sentence_as_list)
print(output)