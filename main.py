import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    from stats import get_num_words
    num_words = get_num_words(book_text)
    from stats import get_chars_dict
    chars_dict = get_chars_dict(book_text)
    from stats import get_sorted_list
    sorted_list = get_sorted_list(chars_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")

main()