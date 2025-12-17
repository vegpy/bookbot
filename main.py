import sys
from stats import count_words, count_car, sort_words, sort_on
def main():
    
    if len(sys.argv) == 2:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    text = get_book_text(book)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    num_car = (count_car(text))
    sort = sort_words(num_car)
    for i in sort:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()

    return file_contents



def count_words(text):
    words = text.split()
    return len(words)



main()







