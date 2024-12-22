def word_count(book_content):
    return len(book_content.split())    

#Not asked to exclude symbols, will include.
def letter_count(book_content):
    letters = {}
    for l in book_content:
        low = l.lower()
        if low in letters:
            letters[low] += 1
        else:
            letters[low] = 1
    return letters

def get_text(path):
    with open(path) as file:
        contents = file.read()
        
    return contents
        
def dict_to_list(dictionary):
    list = []
    for key in dictionary:
        list.append({"character":key , "times" :dictionary[key]})
    list.sort(reverse=True, key=sort_on)
    
    return list

def sort_on(d):
    return d["times"]
        
    
def main():
    book_path = "books/frankenstein.txt"
    book = get_text(book_path)
    words = word_count(book)
    letters = letter_count(book)
    report = dict_to_list(letters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for entry in report:
        print(f"The {entry["character"]} character was found {entry["times"]} times")
    
main()