"""A program to manage customers' pizza orders."""

import math


def stars():
    print("*" * 60)


def dotted():
    print("." * 60)


def get_string(m):
    """Ask for user input as a string.

        :param m: list
        :return: string

        """
    my_string = str(input(m))
    return my_string


def get_integer(m):
    """Ask for user input as an integer.

            :param m: list
            :return: string

            """
    my_integer = int(input(m))
    return my_integer


def single_loop_print(p):
    """Print the list.

        :param L: list
        :return: None

        Print the list in a nice format and only once.
        """
    output = "{: ^10} {:^15} {:^15}".format("PRICE", "PIZZAS", "DESCRIPTION")
    print(output)
    stars()
    for i in range(0, len(p)):
        output = "{}:   {: ^10} --- {:<10} --- {:<10}".format(i, p[i][0], p[i][1], p[i][2])
        print(output)


def add_to_order(mo,p):
    """Add pizza to order.

        :param L: list
        :return: None

        The required list must be two-dimensional,
        and the sub list must be of the form [str, int],
        requests user input for index and quantity,
        adds new pizza and quantity to the list,
        prints confirmation.
        """
    print("Start to fill out order")
    dotted()
    pizza_choice_index = get_integer("Enter pizza index number:")
    chosen_pizza = p[pizza_choice_index][1]
    quantity = get_integer("How many {} pizzas would you like?".format(chosen_pizza))
    temp_list = [chosen_pizza, quantity]
    mo.append(temp_list)


def review_order(mo):
    print("Here is your order so far:")
    for i in range(0, len(mo)):
        order = ("{: ^10} --- {:<10} ".format(mo[i][0], mo[i][1]))
        print(order)


def quit_or_menu():
    """Choose to either quit or view menu.
        :param: None
        :return: None
        """
    # this list is a list of the customer's ordered pizzas
    my_order = []

    price_of_regular = 18.5
    price_of_gourmet = price_of_regular + 7

    pizzas = [
        (price_of_regular, "USA", "A tasty meat lovers pizza"),
        (price_of_regular, "Australia", "Pineapple, shrimp and BBQ sauce"),
        (price_of_gourmet, "Russia", "Mockba four fish pizza with sardines, tuna, mackerel and salmon"),
        (price_of_gourmet, "India", "Pickled ginger and paneer")
    ]

    option_menu = [
        ("V", "View pizza menu"),
        ("O", "Start order"),
        ("R", "Review order so far"),
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
        dotted()
        if option_choice == "V":
            single_loop_print(pizzas)
            dotted()
        elif option_choice == "O":
            single_loop_print(pizzas)
            add_to_order(my_order, pizzas)
        elif option_choice == "R":
            review_order(my_order)
            dotted()
        elif option_choice == "Q":
            for i in range(0, len(confirm_quit)):
                print("{:3} : {}".format(confirm_quit[i][0], confirm_quit[i][1]))
            ask_quit_confirmation = get_string("Are you sure you want to quit?").upper()
            dotted()
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