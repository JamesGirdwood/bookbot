from collections import defaultdict
def count_words_in_text(book_text):
    #Split the text into words using whitespace as a delimiter
    words = book_text.split()

    #Get the number of words in the text
    num_words = len(words)

    #Print the amount of words in the books
    print(f"Found {num_words} total words")
    return num_words

def count_character_frequencies(book_text):
    #Initialize a dictionary to store character frequencies
    char_frequency = defaultdict(int)

    #Convert the text to lowercase and iterate through each character
    for char in book_text.lower():
        char_frequency[char] += 1
    
    #Sort the character frequencies in descending order by count
    sorted_char_frequencies = [{'char': char, 'count': count} for char, count in sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)]

    return sorted_char_frequencies
