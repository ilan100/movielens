# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# EX1A
def list_rem_nonstr(listname):
    newlist = []
    for item in listname:
        if type(item) != str:
            newlist.append(item)
    for item in newlist:
        listname.remove(item)

# EX1B
def list_rem_nonstr2(listname):
    for x in listname[:]:
        if not isinstance(x, str):
            listname.remove(x)
# EX2
def count_letters(str):
    counts = {}
    for ch in str:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

# EX3
def merge_lists(list1, list2):
    newlist = []
    templist = list1
    # Select the shorter list to scan for efficiency
    if (len(list1) > len(list2)):
        templist = list2
    b = len(list2)
    for item in templist:
        if item in list2:
            newlist.append(item)
    return newlist

# EX4
def dict_to_unique_list(dic):
    return list(set(dic.values()))

# EX5 (any index for rotation)
def left_rotate(lst, k):
    return lst[k:] + lst[:k]

# EX6
def list_rem_print(lst):
    newlist = lst.copy()
    for x in newlist[::2]:
        print(x)
        lst.remove(x)

# EX7
def dic_to_tuple_list(dic):
    return list(dic.items())

#EX8
def find_dict_max_min(dic):
    key = max(dic, key=dic.get)
    print('max value key', key)
    key = min(dic, key=dic.get)
    print('min value key:', key)

# EX9
def remove_chars(str1, str2):
    remove = set(str2) # Using set gives an O(1) speed instead of O(n) for list
    return "".join(ch for ch in str1 if ch not in remove)


#----------------------------------------------------------------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [1, 'sty', 'ghf', 34, 334.5, 'tyy', 8]
    list_rem_nonstr2(a)
    print('modified list:', a)
    text = "hello world"
    print(count_letters(text))
    list1 = [3, 6, 67, 12, 34, 7, 9]
    list2 = [1, 3, 25, 62, 67, 127, 34, 7, 9]
    print(merge_lists(list1, list2))
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 25, 'f': 4, 'g': 2, 'h': 3}
    print(dict_to_unique_list(dic))
    list3 = [2, 4, 6, 8, 12]
    print(left_rotate(list3, 1))
    list_rem_print(list3)
    print(list3)
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 25, 'f': 4, 'g': 2}
    find_dict_max_min(dic)
    print(dic_to_tuple_list(dic))
    str1 = 'hello world'
    str2 = 'eld'
    print(remove_chars(str1, str2))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
