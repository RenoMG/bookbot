from stats import get_num_words, char_counter, sort_char_count, organise_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(input):
    if len(input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    input = input[1]

    get_data = organise_char_count(input)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input}...")
    print("----------- Word Count ----------")
    print(get_num_words(input))
    print("--------- Character Count -------")
    for data in get_data:
        if not data["char"].isalpha():
            continue

        print(f"{data["char"]}: {data["num"]}")
    print("============= END ===============")

#print("Please enter a file path for a txt file.")
main(sys.argv)