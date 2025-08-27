from stats import count_words, count_chars, build_sorted
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        text = get_book_text(path)
        counts = count_chars(text)
        sorted_chars = build_sorted(counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        total_words = len(count_words(text))
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")

        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")

        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
