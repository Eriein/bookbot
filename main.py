from stats import count_number_of_words, get_book_text

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_number_of_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()