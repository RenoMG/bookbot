from stats import get_num_words

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(input):
    print(get_num_words(input))

#print("Please enter a file path for a txt file.")
main("books/frankenstein.txt")