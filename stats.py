def word_count(book_txt):
    words = book_txt.split()
    num_words = len(words)
    return num_words

def character_count(book_txt):
    char_count = {}
    book_txt = book_txt.lower()
    for character in book_txt:
        if character not in char_count:
            char_count[character] = 1
        else:
            char_count[character] += 1
    return char_count

def sorts_list(book_txt):
    sort_list = []
    for char, count in book_txt.items():
        sort_list.append({"char": char, "num": count})
    sort_list.sort(reverse=True, key=sort_num)
    return sort_list
def sort_num(sorts_list):
    return sorts_list["num"]
