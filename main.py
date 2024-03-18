def count_words(book):
    words = len(book.split())
    print(words)

def count_letters(book):
    lowered_string = book.lower()
    words = lowered_string.split()

    all_letters = []

    for word in words:
        letters = list(word)
        for letter in letters:
            all_letters.append(letter)

    count_letters = {}

    for letter in all_letters:
        if letter in count_letters:
            dict[letter] += 1
        else:
            dict[letter] = 1

    print(count_letters)

def main():
    book = ""
    with open("./books/frankenstein.txt") as f:
        book = f.read()

    count_words(book)
    count_letters(book)

main()

