def count_words(book) -> int:
    return len(book.split())

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

def print_report(path, book):
    print(f"--- Begin report of {path} ---")
    words = count_words(book)
    print(f"{words} words found in the document")

def main():
    path = "./books/frankenstein.txt"
    book = ""
    with open(path) as f:
        book = f.read()
        print_report(path, book)

main()

