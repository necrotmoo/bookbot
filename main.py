from stats import get_num_words
from stats import get_sort_list
from stats import get_num_letter
import sys
def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

book_path = sys.argv
try:
	result = book_path[1]
except Exception as e:
	print(e)
	print("Usage: python3 main.py <path_to_book>")
	print("exit code: 1")
	exit(code=1)

book = get_book_text(book_path[1])
word_count = get_num_words(book_path[1])
letter_count = get_num_letter(book)
sorted_letters = get_sort_list(letter_count)

#print("============ BOOKBOT ============")
#print("Analyzing book found at books/frankenstein.txt...")
#print("----------- Word Count ----------")
#print("Found", word_count, "total words")
#print("--------- Character Count -------")

if len(book_path) == 2:
	for k,v in sorted_letters.items():
		print(f"{k}:", v)
	print(word_count)

	
	


	