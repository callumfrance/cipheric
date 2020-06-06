from english_detection import *

def load_frequencies():
    freq_file = open('letter_frequencies.txt')
    letters = {}
    for line in freq_file:
        line = line.strip().split(",")
        letters[line[0]] = (line[1], line[2])
    freq_file.close()
    # print letters
    # print letters['e'][1]

load_frequencies()

def count_frequencies(message):
    message = message.upper()
    letter_counts = {}
    for i in UPPERLETTERS:
        letter_counts[i] = 0
    for j in message:
        if j in UPPERLETTERS:
            letter_counts[j] += 1
    # print(letter_counts)
    return(letter_counts)

def sorted_frequencies(message):
    letter_counts = count_frequencies(message)
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1])[::-1]
    print(sorted_letters)
    # print({k: v for k, v in sorted(letter_counts.items(), key=lambda item: item[1])})

if __name__ == '__main__':
    test1 = ""
    with open("source_texts/1984.txt", 'r') as f:
        test1 = f.read()

    sorted_frequencies(test1)
