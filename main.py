from stats import count_number_of_words, get_book_text, count_characters, sorted_list, print_sorted_data

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_number_of_words(text)
    num_chars = count_characters(text)
    sorted_data = sorted_list(num_chars)
    print_report(book_path, num_words, sorted_data)
    

def print_report(book_path, num_words, sorted_data):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_sorted_data(sorted_data)
    print("============= END ===============")


if __name__ == "__main__":
    main()