def count_words(content):
    return len(content.split())

def count_char (content):
    content = content.lower()
    
    
    char_count ={}
    for char in content:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_dict  (char_count):
    def sort_on(items):
        return items["num"]
    dict = []
    for i in char_count:
        dict_char = {"char":i,"num":char_count[i]}
        dict.append(dict_char)
    dict.sort(reverse=True,key=sort_on)
    return dict


