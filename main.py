import sys

from stats import num_of_words, char_appears_count, sorted_char_dict, sorting

# Function to read and open the contents of a file
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Getting the number of words from the .txt filepath 
    num_words = num_of_words(get_book_text(sys.argv[1]))

    # # Getting the number of characters from the .txt filepath
    char_count = char_appears_count(get_book_text(sys.argv[1]))

    # Sorting from highest to lowest 
    sorted_char_count = sorting(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {(sys.argv[1])}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    #To print in the desired outcome by keys and values through looping
    for sorted_char in sorted_char_count:
        print(f"{sorted_char["char"]}: {sorted_char["num"]}")

main()