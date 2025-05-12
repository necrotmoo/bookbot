def get_num_words(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
		words_split = file_contents.split(None)
		num_words = len(words_split)
	return num_words

def get_num_letter(text):
	char_count = {}
	for char in text:
		char = char.lower()
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count

def get_sort_list(dict_list):
	sorted_list = {}
	char = {}
	sorted_dict = {}
	for k, v in dict_list.items():
		if k.isalpha() == True:			
			sorted_list[k] = v

	char = sorted(sorted_list, key=str)	
	for c in char:
		for k, v in dict_list.items():
			if c == k:
				sorted_dict[f"{k}"] = f"{v}"
			
	

	return sorted_dict