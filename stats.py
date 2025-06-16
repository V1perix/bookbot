

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on_num(d):
    return d["num"]

def get_sorted_list(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(key=sort_on_num, reverse=True)
    return dict_list