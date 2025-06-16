from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_list = get_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()


main()