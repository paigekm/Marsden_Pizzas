"""A program to manage customers' pizza orders."""

import math


def get_string(m):
    """Ask for user input as a string.

    :param m: list
    :return: string

    """
    my_string = input(m)
    return my_string


def single_loop_print(L):
    """Print the list.

    :param L: list
    :return: None

    Print the list in a nice format and only once.
    """
    output="{: ^10} {:^10}".format("Price", "Pizzas")
    print(output)
    for i in range(0, len(L)):
        output = "{: ^10} --- {:^10}".format(L[i][0], L[i][1])
        print(output)


def quit_or_menu():
    """Choose to either quit or view menu.
    :param: None
    :return: None
    """

    my_order = []

    pizzas = [
        ("18.5", "USA"),
        ("18.5", "Australia"),
        ("25.5", "Russia"),
        ("25.5", "India")
    ]

    option_menu = [
        ("F", "View pizza menu"),
        ("Q", "Quit")
    ]

    confirm_quit = [
        ("Q", "Continue quit"),
        ("B", "Go back to menu page")
    ]

    run = True
    while run == True:
        for i in range(0, len(option_menu)):
            print("{:3} : {}".format(option_menu[i][0], option_menu[i][1]))
        option_choice = get_string("What would you like to do? -> ").upper()
        print("." * 60)
        if option_choice == "F":
            single_loop_print(pizzas)
            print("." * 60)
        elif option_choice == "Q":
            for i in range(0, len(confirm_quit)):
                print("{:3} : {}".format(confirm_quit[i][0], confirm_quit[i][1]))
            ask_quit_confirmation = get_string("Are you sure you want to quit?").upper()
            if ask_quit_confirmation == "Q":
                print("Thank you for visiting Marsden Pizzas. Hope to see you again!")
                run = False
            elif ask_quit_confirmation == "B":
                run = True
            else:
                print("You have requested an invalid choice.")
        else:
            print("You have requested an invalid choice.")


quit_or_menu()