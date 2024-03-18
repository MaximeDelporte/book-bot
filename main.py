def count_words(book):
    words = len(book.split())
    print(words)

def main():
    file_contents = ""
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    count_words(file_contents)

main()

