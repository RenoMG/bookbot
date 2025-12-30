from stats import get_num_words, char_counter, sort_char_count, organise_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main(input):
    print(organise_char_count(input))

#print("Please enter a file path for a txt file.")
main("books/frankenstein.txt")