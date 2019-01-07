# TODO: zestaw nawiasow mowi miec tyle samo otwierajacych co zamykajacych nawiasow.
# TODO: ciag nawiasow nie moze zawierac ] na poczatku stringu, [ na koncu stringu.


def get_user_brackets():
    user_brackets = input("Please enter string of brackets '[' or ']': ")
    return user_brackets


def check_equality_of_brackets(bracket_string):
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


def check_user_brackets(bracket_string):
    if len(bracket_string) % 2 != 0:
        # print('Nieparzyste')
        result = False
    elif bracket_string[0] == ']':
        # print('prawy na poczatku')
        result = False
    elif bracket_string[-1] == '[':
        # print('lewy na koncu')
        result = False
    elif check_equality_of_brackets(bracket_string) is False:
        # print('nierowna liczba bracketow')
        result = False

    return result


def main():
    input_brackets = get_user_brackets()
    brackets_check_result = check_user_brackets(input_brackets)
    print(brackets_check_result)


if __name__ == '__main__':
    main()
