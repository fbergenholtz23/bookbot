from stats import get_num_word
from stats import count_chars
from stats import sorted_dic

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_word(text)
    char_dic = count_chars(text)
    char_dic_sorted = sorted_dic(char_dic)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in char_dic_sorted:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()
