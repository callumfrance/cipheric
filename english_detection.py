"""
From https://inventwithpython.com/hacking/chapter12.html
"""
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def load_dict():
    dict_file = open('dictionary.txt')
    english_words = {}
    for word in dict_file.read().split('\n'):
        english_words[word] = None
    dict_file.close()
    return english_words

ENGLISH_WORDS = load_dict()

def get_english_count(message):
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possible_words)

def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return ''.join(letters_only)

def is_english(message, word_percentage=20, letter_percentage=85):
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match

def find_english_output(message):
    x = is_english(message)
    if x:
        print(message)
        return True
    return False


if __name__ == '__main__':
    test1 = "This is a test string"
    test2 = "odjbfp25p `-329884hp;b"

    find_english_output(test1)
    find_english_output(test2)
