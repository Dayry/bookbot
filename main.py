def count_words(text):
    return len(text.split())

def count_letters(text):
    count_dict = {}
    lower_text = text.lower()

    for letter in lower_text:
        if letter.isalpha():
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

    return count_dict

def print_report(text, path_name):
    

    print(f"--- Begin report of {path_name} ---")
    print(f"{count_words(text)} words found in the document\n")

    letter_counts = chars_dict_to_sorted_list(count_letters(text))

    for item in letter_counts:
        print(f"The {item['char']} was found {item['num']} times")

    print(f"--- End report ---")

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]


def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()

        print_report(file_contents, book_path)

main()




