def get_num_word(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_nums(item):
    return item["num"]

def sorted_dic(dic):
    dic_list = []
    for char in dic:
        tmp_dic = {"char": char, "num": dic[char]}
        dic_list.append(tmp_dic)
    dic_list.sort(reverse=True, key=get_nums)
    return dic_list
    