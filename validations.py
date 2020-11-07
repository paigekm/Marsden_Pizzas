"""Two validated versions of the get integer and get string functions."""


def get_validated_integer(message, min, max):
    """Get user input.

    And tests that the length of the integer
    is greater than our min and less than our maximum.
    loops until an acceptable input is received

    :param message: str
    :param min: int
    :param max: int
    :return: int
    """
    while True:
        try:
            integer_entry = int(input(message))
            # if a non integer is entered prints an error message
        except ValueError:
            print("This is not a valid entry. A whole number is needed.")
            continue
        # if the entry is smaller than the index numbers in the list,
        # prints an error message
        if integer_entry < min:
            print("The number you entered: {}, is too small. "
                  "Please enter an index number that is "
                  "{} or greater.".format(integer_entry, min))
        # if the entry is larger than the index numbers in the list,
        # prints an error message
        elif integer_entry > max:
            print("The number you entered: {}, is too big. "
                  "Please enter an index number that is "
                  "{} or smaller.".format(integer_entry, max))
        # if the integer is in a valid form, returns it to be used
        else:
            return integer_entry


def get_validated_integer_pizzalimits(message, min, max):
    """Get user input.

    And tests that the length of the integer
    is greater than our min and less than our maximum.
    loops until an acceptable input is received

    Includes error messages for an index number entry
    Includes error messages for max number of pizzas of one type

    :param message: str
    :param min: int
    :param max: int
    :return: int
    """
    while True:
        try:
            integer_entry = int(input(message))
            # if a non integer is entered, prints error message
        except ValueError:
            print("This is not a valid entry. A whole number is needed")
            continue
        # if orders less than the min amount of pizzas per type,
        # prints constructive error message
        # asks for re-entry
        if integer_entry < min:
            print("The number you entered: {}, is too small. "
                  "You have to order "
                  "{} or more pizza/s of this type."
                  .format(integer_entry, min))
        # if orders more than the max amount of pizzas per type,
        # prints constructive error message
        # asks for re-entry
        elif integer_entry > max:
            print("The number you entered: {}, is too big. "
                  "You are only allowed purchase a maximum of "
                  "{} pizza/s of one type.".format(integer_entry, max))
        # if number of pizzas of each type is valid
        else:
            return integer_entry


def get_validated_string(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    greater than 1 or less than a maximum.

    :param message: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        string_entry = input(message).replace(" ", "")
        # if the entry has fewer characters than required,
        # prints an error message
        if len(string_entry) < min:
            print("Please ensure your entry has at least "
                  " {} character/s.".format(min))
        # if the entry has more characters than required,
        # prints an error message
        elif len(string_entry) > max:
            print("Please ensure your entry has no "
                  "more than {} character/s.".format(max))
        # asks for string entry again if error message is printed, as above
        # if string entry is valid after passing through this validation,
        # is returned to be used
        else:
            return string_entry


def get_validated_string_p_or_d(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    one character only.

    Includes error messages for if not P or D,
    asks to reenter entry if any error message occurs.

    :param message: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        # ensures string entry is capitalised before validating
        string_entry = input(message).upper()
        string_entry = string_entry.replace(" ", "")
        # if the entry has fewer characters than is required,
        # prints an error message
        if len(string_entry) < min:
            print("You have not entered enough characters. "
                  "Please enter at least {} character/s.".format(min))
        # if the entry has more characters than is required,
        # prints an error message
        elif len(string_entry) > max:
            print("You have entered too many characters. "
                  "Please enter no more than {} character/s.".format(max))
        # if the entry is either one of the two valid options,
        # returns this value as it is valid
        elif string_entry in ["P", "D"]:
            return string_entry
        # if the entry is the correct number of characters in length,
        # but is not either of P or D (the 2 valid entries),
        # prints an error message
        # whenever prints an error message, re-asks for the entry from user
        else:
            print("Your input is not part of the acceptable list, "
                  "please enter P or D")


def get_validated_string_y_or_n(message, min, max):
    """Get user input.

    And tests that the length of the string is,
    only 1 character.

    Includes error messages for a if not Y or N,
    and re-asks confirmation question if not Y or N.

    :param message: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        # capitalises user entry before running through validation
        string_entry = input(message).upper()
        string_entry = string_entry.replace(" ", "")
        # if the entry has fewer characters than is wanted,
        # prints an error message
        if len(string_entry) < min:
            print("You have not entered enough characters. "
                  "Please enter at least {} character/s.".format(min))
        # if the entry has more characters than is wanted,
        # prints an error message
        elif len(string_entry) > max:
            print("You have entered too many characters. "
                  "Please enter no more than {} character/s.".format(max))
        # if the entry is either Y or N
        # user entry is returned to be used as it is valid
        # and can be recognised by the program
        elif string_entry in ["Y", "N"]:
            return string_entry
        # if the entry is the correct number of characters in length,
        # but is not either Y or N (the 2 valid entries)
        # prints error message
        # whenever prints an error message, re-asks for the entry from user
        else:
            print("Your input is not part of the acceptable list, "
                  "please enter Y or N")


def get_validated_string_phone(message_phone, min, max):
    """Get user input.

     Ensure a valid string of only numbers
     is returned.
     Tests for min and max character len,
     so the entry can only be 9-15 characters long,
     otherwise an error message is printed.
     When an error message prints,
     the phone number entry is re-asked for.

    :param message_phone: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        # ensures the phone number has no spaces
        string_entry = input(message_phone).replace(" ", "")

        # assume the phone number is not valid to begin with
        not_valid_phone = False
        for i in range(0, len(string_entry)):
            # if any of the characters in the phone number
            # is not a valid number
            # phone number is invalid
            if string_entry[i] not in ["0", "1", "2", "3",
                                       "4", "5", "6", "7", "8", "9", "-"]:
                not_valid_phone = True

        # if the phone number is invalid,
        # prints error message and re-asks for entry of phone number
        if not_valid_phone == True:
            print("Please enter only numbers and dashes in your phone number.")
            continue
            # if the entry has fewer characters than is required,
            # prints an error message
        if len(string_entry) < min:
            print("Your entry is too short. "
                  "Please enter at least {} character/s.".format(min))
            continue
        # if the entry has more characters than is required,
        # prints an error message
        elif len(string_entry) > max:
            print("You can only enter {} character/s".format(max))
            continue
        # once the user's entry is valid,
        # returns this validated entry to be used in the main function
        else:
            return string_entry


# only runs if this validations file runs,
# doesn't run if called into another file
if __name__ == "__main__":
    test_string = get_validated_string_p_or_d("Please enter a "
                                              "p or d", ["P", "D"])
    print(test_string)
