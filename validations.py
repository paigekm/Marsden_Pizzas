"""Two validated versions of the get integer and get string functions."""


def get_validated_integer(message, min, max):
    """Get user input.

    And tests that the length of the integer
    is greater than our min and less than our maximum.
    loops until an acceptable input is received

    :param M: str
    :param min: int
    :param max: int
    :return: int
    """
    while True:
        try:
            integer_entry = int(input(message))
        except ValueError:
            print("This is not a valid entry. A whole number is needed")
            continue
        if integer_entry < min:
            print("The number you entered: {}, is too small. "
                  "Please enter a number that is "
                  "{} or greater.".format(integer_entry, min))
        elif integer_entry > max:
            print("The number you entered: {}, is too big. "
                  "Please enter a number that is "
                  "{} or smaller.".format(integer_entry, max))
        else:
            return integer_entry


def get_validated_string(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    greater than 1 or less than a maximum.

    :param M: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        string_entry = input(message)
        if len(string_entry) < min:
            print("Please ensure your entry has more "
                  "than {} characters.".format(min))
        elif len(string_entry) > max:
            print("Please ensure your entry has no "
                  "more than {} characters.".format(max))
        else:
            return string_entry


if __name__ == "__main__":
    test_string = get_validated_string("Please enter a fruit:", 2, 40)
    print(test_string)
