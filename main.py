def main():
     with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
     
book = main()

def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    counts = {}
    lower_case_book = book.lower()  
    for char in lower_case_book:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1 

    return counts

words = count_words(book)
dict = count_chars(book)
list_of_dict = [{"char": key, "count": value} for key, value in dict.items()]

def sort_on(dict):
    return dict["count"]  # we use "count" because that's the key we used in our dictionaries

list_of_dict.sort(reverse=True, key=sort_on)

def build_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} found in the document")
    print('')
    
    for item in list_of_dict:
        print(f"The '{item["char"]}' character happened {item["count"]} times.")
        print('')
    print("--- End report ---")
build_report()