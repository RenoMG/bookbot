def get_num_words(file_path):
    with open(file_path) as f:
        return f"Found {len(f.read().split())} total words"