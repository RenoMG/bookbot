def get_num_words(file_path):
    with open(file_path) as f:
        return f"Found {len(f.read().split())} total words"

def char_counter(file_path):
    char_count_db = {}

    with open(file_path) as f:
        book_text = f.read()

    for char in book_text:
        if char.lower() not in char_count_db:
            char_count_db[char.lower()] = 0

        if char.lower() in char_count_db:
            char_count_db[char.lower()] = char_count_db[char.lower()] + 1

    return char_count_db