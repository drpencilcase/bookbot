from stats import count_words, count_char, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath,word_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # loop through sorted_chars and print each one
    for i in sorted_dict:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")



def main():
    if len(sys.argv) != 2:
       return print("Usage: python3 main.py <path_to_book>"),sys.exit(1)
    else:
        file_path = sys.argv[1]
        content = get_book_text(file_path)
        word_count = count_words(content)
        word_count_string = f"{word_count} words found in the document"
        char_count = count_char(content)
        sorted_dict = sort_dict(char_count)
        return print_report(file_path,word_count,sorted_dict)

main()  
