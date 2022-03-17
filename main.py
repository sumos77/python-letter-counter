def letter_counter(contents):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    letters = {}
    for letter in alphabet:
        letters[letter] = 0

    for letter in contents.lower():
        if letter in letters:
            letters[letter] += 1
    print(letters)
    return


with open('lorem_ipsum.txt') as file:
    file_contents = file.read()
    print(file_contents)

letter_counter(file_contents)
