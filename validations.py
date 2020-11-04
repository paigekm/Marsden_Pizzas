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
                  "Please enter an index number that is "
                  "{} or greater.".format(integer_entry, min))
        elif integer_entry > max:
            print("The number you entered: {}, is too big. "
                  "Please enter an index number that is "
                  "{} or smaller.".format(integer_entry, max))
        else:
            return integer_entry


def get_validated_integer_pizzalimits(message, min, max):
    """Get user input.

    And tests that the length of the integer
    is greater than our min and less than our maximum.
    loops until an acceptable input is received

    Includes error messages for an index number entry

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
                  "You have to order "
                  "{} or more pizzas of this type.".format(integer_entry, min))
        elif integer_entry > max:
            print("The number you entered: {}, is too big. "
                  "You are only allowed purchase a maximum of "
                  "{} pizzas of one type.".format(integer_entry, max))
        else:
            return integer_entry


def get_validated_string(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    greater than 1 or less than a maximum.

    Includes error messages for a number of pizzas in the order entry

    :param M: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        string_entry = input(message)
        if len(string_entry) < min:
            print("Please ensure your entry has at least "
                  " {} characters.".format(min))
        elif len(string_entry) > max:
            print("Please ensure your entry has no "
                  "more than {} characters.".format(max))
        else:
            return string_entry


def get_validated_string_P_or_D(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    greater than 1 or less than a maximum.

    Includes error messages for a if not P or D

    :param M: str
    :return: str
    """
    while True:
        string_entry = input(message)
        string_entry = string_entry.upper()
        if len(string_entry) < min:
            print("You have not entered enough characters. Please enter 1 only.")
        elif len(string_entry) > max:
            print("You have entered too many characters. Please enter 1 only.")
        elif string_entry in ["P", "D"]:
            return string_entry
        else:
            print("Your input is not part of the acceptable list, please enter P or D")


def get_validated_string_Y_or_N(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    greater than 1 or less than a maximum.

    Includes error messages for a if not P or D

    :param M: str
    :return: str
    """
    while True:
        string_entry = input(message)
        string_entry = string_entry.upper()
        if len(string_entry) < min:
            print("You have not entered enough characters. Please enter 1 only.")
        elif len(string_entry) > max:
            print("You have entered too many characters. Please enter 1 only.")
        elif string_entry in ["Y", "N"]:
            return string_entry
        else:
            print("Your input is not part of the acceptable list, please enter Y or N")


def get_validated_string_phone(message_phone, min, max):
    """
        to ensure only a valid string of numbers
        is returned.
        tests for min and max character len,
        3 arguments: string message, min int, max int
        """
    while True:
        string_entry = input(message_phone)
        string_entry = string_entry.replace(" ", "")
        if len(string_entry) < min:
            print("You have not entered enough characters")
            continue
        elif len(string_entry) > max:
            print("You can only enter {} character/s".format(max))
            continue

        not_valid_phone = False
        for i in range(0, len(string_entry)):
            if string_entry[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                not_valid_phone = True

        if not_valid_phone == True:
            print("You should not have any letters in your phone number.")
            continue
        else:
            return string_entry


if __name__ == "__main__":
    test_string = get_validated_string_P_or_D("Please enter a p or d", ["P", "D"])
    print(test_string)
