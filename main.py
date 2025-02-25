from stats import get_number_of_words, get_letter_stats, get_sorted_stats
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if (len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookfile = sys.argv[1]
    mybook = get_book_text(bookfile)
    num_words = get_number_of_words(mybook)
    char_stats = get_letter_stats(mybook)
    sorted_stats = get_sorted_stats(char_stats)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_stats:
        if (char["name"]).isalpha() == True:
            print(char["name"] + ": " + str(char["num"]))
main()
