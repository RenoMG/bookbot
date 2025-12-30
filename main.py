from stats import get_num_words, char_counter

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(input):
    print(char_counter(input))

#print("Please enter a file path for a txt file.")
main("books/frankenstein.txt")