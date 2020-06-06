from english_detection import *

def shifter(message):
    message = message.upper()
    message = remove_non_letters(message)
    for i in range(26):
        CAESARLETTERS = UPPERLETTERS[i : ] + UPPERLETTERS[0 : i]
        shifted = ""
        for j in message:
            if j in CAESARLETTERS:
                letterpos = CAESARLETTERS.find(j)
                shifted += UPPERLETTERS[letterpos]
            else:
                shifted += j
        if find_english_output(shifted):
            break


if __name__ == '__main__':
    test1 = "This is a test string"
    test2 = "WKLV LV D VHFRQG FDHVDU VKLIWHG WHVW VWULQJ"
    test3 = "SGHR HR Z SGHQC BZDRZQ RGHESDC SDRS RSQHMF"

    shifter(test1)
    shifter(test2)
    shifter(test3)
