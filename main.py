def get_words_count_from(book) -> int:
    return len(book.split())


def get_letters_count_from(book):
    lowered_string = book.lower()
    words = lowered_string.split()

    all_letters = []

    for word in words:
        letters = list(word)
        for letter in letters:
            all_letters.append(letter)

    dictionary_letters = {}

    for letter in all_letters:
        if not letter.isalpha():
            continue

        if letter in dictionary_letters:
            dictionary_letters[letter] += 1
        else:
            dictionary_letters[letter] = 1

    sorted_array = sorted(dictionary_letters.items(), key=lambda x:x[1])
    ordered_array = sorted_array[::-1]
    return ordered_array


def print_report(path, book):
    print(f"--- Begin report of {path} ---")
    words = get_words_count_from(book)
    print(f"{words} words found in the document\n")

    letters_count = get_letters_count_from(book)
    for key, value in letters_count:
        time_word = "times"
        if value == 1:
            time_word = "time"

        print(f"The '{key}' character was found {value} {time_word}")

    print("--- End report ---")

def main():
    path = "./books/frankenstein.txt"
    with open(path) as f:
        book = f.read()
        print_report(path, book)


main()
