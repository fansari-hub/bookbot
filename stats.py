def get_number_of_words(string):
    word_list = string.split()
    return len(word_list)

def get_letter_stats(string):
    char_list = list(string)
    char_dict = {}
    for char in char_list:
        char_lowercase = char.lower()
        if (char_lowercase in char_dict):
            char_dict[char_lowercase] += 1
        else:
            char_dict[char_lowercase] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_stats(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"name": char, "num" : dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list