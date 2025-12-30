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

def organise_char_count(file_path):
    get_char = char_counter(file_path)

    list_of_counts = []
    
    for char in get_char:
        list_of_counts.append({"char": f"{char}", "num": get_char[char]})

    list_of_counts.sort(reverse=True, key=sort_char_count)
    return list_of_counts

def sort_char_count(items):
    return items["num"]