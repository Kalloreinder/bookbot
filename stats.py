def count_words(document):
    return document.split()


def count_characters(document):
    doc = document.lower()
    letters = {}
    
    for letter in doc:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters