def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    with open(file_path) as f:
        return f"Found {len(f.read().split())} total words"


def main(input):
    print(get_book_text(input))

#print("Please enter a file path for a txt file.")
main("books/frankenstein.txt")