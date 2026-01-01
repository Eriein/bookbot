from stats import count_number_of_words, get_book_text, count_characters

def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = count_number_of_words(text)
    

    num_chars = count_characters(text)
    print(num_chars)

if __name__ == "__main__":
    main()