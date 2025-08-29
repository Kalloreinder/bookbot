from stats import count_words

def get_book_text(filepath):

    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    return file_contents

def main():

    current_book = get_book_text("books/frankenstein.txt")
    num_words = count_words(current_book)
    print(f"{len(num_words)} words found in the document")


if __name__ == "__main__":
    main()
