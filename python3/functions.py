
# EX1
def rem_words_from_list(lst: list, words_to_rem: set):
    return list(filter(lambda x: x not in words_to_rem, lst))

#EX2
def sort_string_numns(lst: list):
    return sorted(lst, key=lambda x: int(x))

#EX3
def calc_neg_pos_sum(lst: list):
    positive_sum = sum(filter(lambda x: x>0, lst))
    negative_sum = sum(filter(lambda x: x<0, lst))
    return positive_sum, negative_sum

# EX4:
def calc_square_even(lst: list):
    evens = [x * x for x in lst if x % 2 == 0]
    return evens

# EX5:
def update_values(d: dict):
    return {k: v * 0.8 for k, v in d.items()}

# EX6:
def gematria_val(dic: dict, hebrew_word: str) -> int:
    return sum(dic.get(ch) for ch in hebrew_word)

# EX7:
def credit_card_validate(num: str) -> bool:
    digits = [int(d) for d in num]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0


#----------------------------------------------------------------------------------------
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = {"house", "tree"}
    mylist = ["garden", "house", "tree", "car", "book"]
    print("EX1:\n", rem_words_from_list(mylist, words))

    list_of_numbers = ["234", "17", "8742", "6", "4", "223"]
    print("EX2:\n", sort_string_numns(list_of_numbers))

    list_numbers = [23, 56, -25, -11, 95, -4]
    a, b = calc_neg_pos_sum(list_numbers)
    print("EX3:\n positive_sum: ", a, "\n negative sum: ", b)

    list_numbers = [1, 2, 3, 4, 5, 6]
    print("EX4:\n", calc_square_even(list_numbers))

    dic = {"prod1": 24, "prod2": 17, "prod3": 20}
    print("EX5:\n", update_values(dic))

    dic = {
        'א': 1,   'ב': 2,   'ג': 3,   'ד': 4,   'ה': 5,
        'ו': 6,   'ז': 7,   'ח': 8,   'ט': 9,   'י': 10,
        'כ': 20,  'ך': 500, 'ל': 30,  'מ': 40,  'ם': 600,
        'נ': 50,  'ן': 700, 'ס': 60,  'ע': 70,  'פ': 80,
        'ף': 800, 'צ': 90,  'ץ': 900, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }
    print("EX6:\n", gematria_val(dic, "אילן"))

    credit_number = "5326108312665580" # i checked a valid number anb it works
    print("EX7:\n card number:", credit_number, "is valid: ", credit_card_validate(credit_number))