# Morse code wiki: https://en.wikipedia.org/wiki/Morse_code
# Program that converts any String input into Morse Code
# Rules:
# 1. 26 basic Latin letters(a to z) + Arabic numbers + . and '
# 2. There is no distinction between upper and loser case letters
# 3. Words displayed as combination of '-' and '.'
# 4. Space between letters as ' ' - 3 dots
# 5. Space between words as '/' - 7 dots

# morse code is included in morsecode.py as a dictionary

from morsecode import morse_code as data

# dict that stores a morse code values of letters/numbers
morse_code_dict = data


def convert(list_of_letters: []) -> str:
    """converts a list of letters into morse code"""
    morse_code_sentence = ""
    for letter in list_of_letters:
        if letter == " ":
            morse_code_sentence += '/ '
        else:
            morse_code_sentence += f"{str(morse_code_dict.get(letter))} "
    return morse_code_sentence


def main():
    # User input (all letters lowered)
    user_sentence = input('Enter the sentence to be converted into morse code: ').lower()
    sentence_as_list = list(user_sentence.strip())
    # print(sentence_as_list)
    output = convert(sentence_as_list)
    print(output)


if __name__ == '__main__':
    main()
