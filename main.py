import sys
from stats import count_words_in_text
from stats import count_character_frequencies
def get_book_text(filepath):
    #opens the given filepath and copies its contents into string file
    with open(filepath) as file:
        book_contents = file.read()
        return book_contents

def main():
    #Check if the correct number of arguments are passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #The second argyment in sys.argv is the path to the book
    file_path = sys.argv[1]
    # Path to the book file
    file_path = "books/frankenstein.txt"
    
    # Print the header with the book file path
    print(f"=========== BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    #Get the book text
    try:
        frankenstein = get_book_text(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        sys.exit(1)

    # Count words in the text and display the result
    print("\n----------- Word Count ----------")
    word_count = count_words_in_text(frankenstein)
    print(f"Found {word_count} total words")
    
    # Count character frequencies and display the result
    print("\n--------- Character Count -------")
    sorted_frequencies = count_character_frequencies(frankenstein)
    
    # Print each character and its count
    for freq in sorted_frequencies:
        print(f"{freq['char']}: {freq['count']}")
    
    print("============= END ===============")
main()
