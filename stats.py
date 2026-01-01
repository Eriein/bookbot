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

def sorted_list(chars):
    sorted_dictionaries = []

    for key, value in chars.items():
        dictionaries = {"chars": key, "num": value}
        sorted_dictionaries.append(dictionaries)

    sorted_dictionaries.sort(reverse=True, key=sort_on)
    return sorted_dictionaries

def sort_on(items):
    return items["num"]

def print_sorted_data(sorted_data):
    for item in sorted_data:
        ch = item["chars"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")