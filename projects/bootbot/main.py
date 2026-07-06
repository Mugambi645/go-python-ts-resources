def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def get_num_words(text):
    words = text.split()
    return len(words)
def main():
    # Relative path to your frankenstein file
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()