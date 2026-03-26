# This is a sample Python script.
from os import MFD_ALLOW_SEALING


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def count_char(string, char):
    if len(char) != 1:
        raise ValueError("The second argument must be a single character.")

    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def rev_num(number):
    num = abs(number)
    newnum = 0
    while num > 0:
        newnum = newnum * 10 + num % 10
        num //= 10
    return newnum

def count_digits(number):
    num = abs(number)
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

def cel2far(number):
    far = number * 9 // 5 + 32;
    return far

def leapyear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def passcheck(string):
    lower = False
    upper = False
    number = False
    special = False
    for c in string:
        ascval = ord(c)
        if (ascval >= ord('A') and ascval <= ord('Z')):
            upper = True
        if (ascval >= ord('a') and ascval <= ord('z')):
            lower = True
        if (ascval >= ord('0') and ascval <= ord('9')):
            number = True
        if (c == '@' or c == '#' or c == '%' or c == '&'):
            special = True

        if (lower and upper and number and special):
            break;

    return (lower and upper and number and special)

def sumdiv(number):
    sum = 0
    for i in range(1, number//2 + 1):
        if number % i == 0:
           sum += i
    sum += number
    return sum

def moneysort(number):
    billsandcoins = [200, 100, 50, 20, 10, 5, 2, 1]
    breakdown = {}
    for i in billsandcoins:
        breakdown[i] = number // i
        number %= i
    return breakdown

def isprime(number):
    prime = True
    for i in range(2, number//2 + 1):
        if number % i == 0:
            prime = False
            break
    return prime


def reverse_float(num):
    s = str(num)

    if '.' in s:
        integer, decimal = s.split('.')
        reversed_num = decimal[::-1] + '.' + integer[::-1]
    else:
        reversed_num = s[::-1]
    return float(reversed_num)

# bad function - dont use !!
def reverse_float2(num):
    s = str(num)
    s = s.replace('.', '')      # remove decimal point
    s = s[::-1]                 # reverse digits
    return float(s)

#------------------------------------------------------------------------------------

def multiply(num1):
    def inner (num2):
        return num1 * num2
    return inner

#------------------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#    number = 123.45
#    print(reverse_float(number))

    money = 3428
    moneyorder = moneysort(money)

    for i in moneyorder:
        if i >= 20:
            print('number of', i, 'bills:', moneyorder[i])
        else:
            print('number of', i, 'coins:', moneyorder[i])

    m1 = multiply(1)
    print(m1(10))
    m2 = multiply(2)
    print(m2(10))
    m2 = multiply(3)
    print(m2(10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
