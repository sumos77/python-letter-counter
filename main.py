alphabet_letters = {
                       'a': 0,
                       'b': 0,
                       'c': 0,
                       'd': 0,
                       'e': 0,
                       'f': 0,
                       'g': 0,
                       'h': 0,
                       'i': 0,
                       'j': 0,
                       'k': 0,
                       'l': 0,
                       'm': 0,
                       'n': 0,
                       'o': 0,
                       'p': 0,
                       'q': 0,
                       'r': 0,
                       's': 0,
                       't': 0,
                       'u': 0,
                       'v': 0,
                       'w': 0,
                       'x': 0,
                       'y': 0,
                       'z': 0
}

alphabet_key_list = list(alphabet_letters.keys())
alphabet_value_list = list(alphabet_letters.values())


def letter_counter(contents):
    for letter in contents:
        for alphabet_letter in alphabet_key_list:
            if alphabet_letter == letter.lower():
                print(alphabet_letter)
    return


with open('lorem_ipsum.txt') as file:
    file_contents = file.read()
    print(file_contents)

letter_counter(file_contents)
