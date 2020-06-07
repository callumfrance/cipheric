from english_detection import *

# LETTERS contains the frequency info for each letter
LETTERS = {}
# L_RANKS is a sorted list of letter frequencies
L_RANKS = [None for i in range(26)]

def load_frequencies():
    freq_file = open('letter_frequencies.txt')
    for line in freq_file:
        line = line.strip().split(",")
        LETTERS[line[0].upper()] = (int(line[1]), float(line[2]))
    freq_file.close()
    # print LETTERS
    for n, i in enumerate(LETTERS):
        # print("L_RANKS[" + str(LETTERS[i][0] - 1) + "]" + " = " + i)
        L_RANKS[int(LETTERS[i][0]) - 1] = i
    # print L_RANKS

load_frequencies()

def count_frequencies(message):
    total_count = 0
    letter_counts = {}
    for i in UPPERLETTERS:
        letter_counts[i] = 0
    for j in message:
        if j in UPPERLETTERS:
            letter_counts[j] += 1
            total_count += 1
    # print(letter_counts)
    return(letter_counts, total_count)

def iterative_replace(message, replacement, to_replace, it_count=0):
    print("Replacing " + to_replace + " with " + replacement)

    for n, x in enumerate(message):
        if (x.isupper()) and (x == to_replace):
            message[n] = replacement
            print(message[n], end="")
        else:
            print(x, end="")

def sequential_manual_replace(message, sorted_letters):
    for it_count in range(26):
        to_replace = sorted_letters[it_count][0]
        replacement = L_RANKS[it_count].lower()

        print("Replace " + to_replace + " with " + replacement + " (Y/N/M/E)?")
        decide = input("\n> ")
        nogos = 0

        if decide.upper() == "Y":
            iterative_replace(message, replacement, to_replace, it_count)
        elif decide.upper() == "M":
            print("Replace which letter?")
            to_replace = input("\n> ")
            print("Replace " + to_replace + " with?")
            replacement = input("\n> ")
            iterative_replace(message, replacement, to_replace, it_count)
        elif decide.upper() == "E":
            print("Choose a filename to export to:")
            with open(input("\n> "), "x") as f:
                f.write(''.join([str(elem) for elem in message]))
            return(True)
        else:
            nogos += 1
            temp_letter = sorted_letters[it_count + nogos]
            sorted_letters[it_count + nogos] = sorted_letters[it_count]
            sorted_letters[it_count] = temp_letter

def sorted_frequencies(message):
    message = list(message.upper())
    letter_counts, total_count = count_frequencies(message)
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1])[::-1]
    print(sorted_letters)
    print(sorted_letters[1])
    sequential_manual_replace(message, sorted_letters)

if __name__ == '__main__':
    test1 = ""
    with open("source_texts/1984_mono.txt", 'r') as f:
        test1 = f.read()

    sorted_frequencies(test1)
