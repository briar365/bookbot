def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        lower_text = lowered_string(text)
        letter = {}
        for character in lower_text:
                if character in letter:
                        letter = letter
                else:
                        count = lower_text.count(character)
                        letter['{character}'] = count
        print(f"{letter}")


def get_num_words(text):
        words = text.split()
        return len(words)
def lowered_string(text):
        lower_string = text.lower()
        return lower_string

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
