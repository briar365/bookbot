with open("books/frankenstein.txt") as f:
     file_contents = f.read()
     words = file_contents.split()
     words = len(words)
     print(words)
