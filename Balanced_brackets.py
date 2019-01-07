def get_user_brackets():
    """ Function get user input as string of '[' and ']' brackets. """
    user_brackets = input("Please enter string of brackets '[' or ']': ")
    return user_brackets


def check_equality_of_brackets(bracket_string):
    """ Function check if amount of '[' and ']' brackets are equal. """
    left_bracket = 0
    right_bracket = 0
    for i in list(bracket_string):
        if i == '[':
            left_bracket += 1
        elif i == ']':
            right_bracket += 1

    if left_bracket == right_bracket:
        result = True
    else:
        result = False

    return result


def advanced_bracket_check(bracket_string):
    """
    Function check if all opened brackets are closed. opening_counter for correct string of brackets should be 0.
    If opening_string get value of -1 function immediatly ends with result set tu False.
    """
    opening_counter = 0
    for i in list(bracket_string):
        if i == '[':
            opening_counter += 1
        elif i == ']':
            opening_counter -= 1

        if opening_counter == -1:
            result = False
            return result

    if opening_counter == 0:
        result = True
    else:
        result = False

    return result


def check_user_brackets(bracket_string):
    """
    Function goes through checks if string of brackes if correct. Strats with simple and fast checks.
    Returns False if any check fails.
    """
    if len(bracket_string) % 2 != 0:
        print('Nieparzyste')
        result = False
    elif bracket_string[0] == ']':
        print('prawy na poczatku')
        result = False
    elif bracket_string[-1] == '[':
        print('lewy na koncu')
        result = False
    elif check_equality_of_brackets(bracket_string) is False:
        print('nierowna liczba bracketow')
        result = False
    elif advanced_bracket_check(bracket_string) is False:
        print('zaawansowane szukanie')
        result = False
    else:
        result = True

    return result


def main():
    input_brackets = get_user_brackets()
    brackets_check_result = check_user_brackets(input_brackets)
    if brackets_check_result:
        print('String of brackets: {0} is OK'.format(input_brackets))
    else:
        print('String of brackets: {0} is NOT OK'.format(input_brackets))


if __name__ == '__main__':
    main()
