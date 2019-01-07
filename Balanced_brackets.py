def get_user_brackets():
    """
    Function get user input as string of '[' and ']' brackets.
    Function checks if user input have only [ and ] brackets.
    """
    while True:
        user_brackets = input("Please enter string of brackets '[' or ']': ")

        if all(char in ['[', ']'] for char in user_brackets):
            break
        else:
            print("Input can only consist of [ and ] brackets. Try again.")

    return user_brackets


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
    Function goes through checks if string of brackes if correct. Strats with simple and fast checks,
    ends with checks in seperate functions. Returns False if any check fails.
    """
    if len(bracket_string) % 2 != 0:
        result = False
    elif bracket_string[0] == ']':
        result = False
    elif bracket_string[-1] == '[':
        result = False
    elif advanced_bracket_check(bracket_string) is False:
        result = False
    else:
        result = True

    return result


def show_final_result(brackets_check_result, input_brackets):
    """ Prints out result of checking given string """
    if brackets_check_result:
        print('String of brackets: {0} is OK'.format(input_brackets))
    else:
        print('String of brackets: {0} is NOT OK'.format(input_brackets))


def main():
    input_brackets = get_user_brackets()
    brackets_check_result = check_user_brackets(input_brackets)
    show_final_result(brackets_check_result, input_brackets)


if __name__ == '__main__':
    main()
