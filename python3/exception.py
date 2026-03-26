
class PasswordError(Exception):
    pass

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
            break

    if not upper:
        raise PasswordError("password must contain Upper case characters")
    if not lower:
        raise PasswordError("password must contain Lower case characters")
    if not number:
        raise PasswordError("password must contain Number characters")
    if (not special):
        raise PasswordError("password must contain @,#,% or &")

    return (lower and upper and number and special)

#------------------------------------------------------------------------------------


if __name__ == '__main__':
    password = input("Enter password: ")
    print("your password:", password)
    check = False
    try:
        check = passcheck(password)
    except PasswordError as e:
        print("password error:", e)
    finally:
        print("password OK:", check)