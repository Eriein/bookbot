def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents


def count_number_of_words(text):
    words = text.split()
    return len(words)