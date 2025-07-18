import sys
from stats import get_book_text, get_num_words, get_character_count, sort_char_counts

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    character_counts = get_character_count(book_text)
    sorted_counts = sort_char_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_counts:
            print(f"{entry['char']}: {entry['num']}")


if __name__ == "__main__":
    main()