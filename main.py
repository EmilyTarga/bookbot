import re

def main():
    file_contents = ""

    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document\n")

    file_contents = re.findall("[a-z]", file_contents.casefold())
    letters = set(file_contents)

    matches = []
    for letter in letters:
        matches.append((letter, file_contents.count(letter)))

    matches.sort(key=lambda x: x[1], reverse=True)
    for match in matches:
        print(f"The '{match[0]}' character was found {match[1]} times")

    print("--- End report ---")

main()
