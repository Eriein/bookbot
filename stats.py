def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents


def count_number_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars_map = {}
    lowered_text = text.lower()
    for ch in lowered_text:
        if ch not in chars_map:
            chars_map[ch] = 1
        else:
            chars_map[ch] += 1
    
    return chars_map