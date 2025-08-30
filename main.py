from stats import count_words, count_characters
BOOK_PATH = "books/frankenstein.txt"


def get_book_text(filepath):

    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    return file_contents


def main():

    current_book = get_book_text(BOOK_PATH)
    num_words = count_words(current_book)
    num_letters = count_characters(current_book)
    print(f"{len(num_words)} words found in the document")
    print(num_letters)


if __name__ == "__main__":
    main()
