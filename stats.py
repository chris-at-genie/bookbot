def get_num_words(text):
    words = text.split()
    return len(words)

# def word_count(path_to_file):
    # with open(path_to_file) as f:
        # words = f.read().split()
        # return len(words)
        # num_words = 0
        # for word in words:
            # num_words += 1
        # return num_words

def get_chars_dict(text):
    chars_dict = {}
    for char in text:
        if not char.lower() in chars_dict:
            chars_dict[char.lower()] = 1
        else:
            chars_dict[char.lower()] += 1
    return chars_dict

def sort_on(d):
    return d["num"]

def get_sorted_list(d):
    sorted_list = []
    for c in d:
        sorted_list.append({"char": c, "num": d[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list