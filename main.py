#counts words and characters(stats)
from stats import word_count, character_count,sorts_list,sort_num
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]

    book_txt = get_book_text (filename)
    word_count_result = word_count(book_txt)
    chars = character_count(book_txt)
    sorting = sorts_list(chars)
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {filename}")
    print("----------- Word Count -----------")
    print (f"Found {word_count_result} total words")
    print("--------- Character Count ---------")

    for i in sorting:
        if i["char"].isalpha():
            print(f"{i ['char']}: {i['num']}")
    print("============= END =============")

main()