def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        lower_text = lowered_string(text)
        letter = {}
        for character in lower_text:
                if character in letter:
                        letter[character] += 1
                else:
                        letter[character] = 1
        letter = dict(sorted(letter.items(), key=lambda item: item[1], reverse = True))
        letter = {key: value for key, value in letter.items() if key.isalpha()}
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        print("")
        for key in my_dict:
                print("The '{key}' character was found {item} times")


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
